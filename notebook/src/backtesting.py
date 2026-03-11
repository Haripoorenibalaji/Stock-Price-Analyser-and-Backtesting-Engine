import sys, os
import statsmodels as ss
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
from colorsetup import colors, palette
sns.set_palette(palette)

# we are using a moving average model here instead of an exponential model
# because an exponential model is better for short term data while a moving everage model would be better for long term stability

# Fibonacci Sequence: Some traders prefer 5, 8, and 13-period SMAs to gain a sharper edge on momentum shifts while reducing false "whipsaw" signals.
# Annual Benchmark: A 255-day SMA is occasionally used to represent a precise full year of trading data.

def sma_crossover(series, short_window, long_window):
    """
    General SMA Crossover strategy.
    """
    df = pd.DataFrame(index=series.index)
    df["price"] = series

    # 1. Calculate SMAs
    df["sma_short"] = series.rolling(window=short_window).mean()
    df["sma_long"] = series.rolling(window=long_window).mean()

    # 2. Drop NaNs to ensure we only trade when both SMAs are ready
    # (Important for 255-day benchmarks)
    df = df.dropna().copy()

    # 3. Generate Signal (1 = Short > Long, 0 = Otherwise)
    df["signal"] = 0
    df.loc[df["sma_short"] > df["sma_long"], "signal"] = 1

    # 4. Shift to avoid Lookahead Bias 
    # You see the signal at market close, but you execute at the next day's open.
    df["position"] = df["signal"].shift(1)

    return df

def test_all_strategies(series):
    all_strategies = {
        "Fibonacci": (8, 21),
        "Annual": (50, 255),
        "Standard": (50, 200)
    }

    results = {}
    for name, (short, long) in all_strategies.items():
        if name == "Fibonacci":
            results[name] = sma_crossover(series, short_window=8, long_window=21)
        elif name == "Annual":
            results[name] = sma_crossover(series, short_window=50, long_window=255)
        elif name == "Standard":
            results[name] = sma_crossover(series, short_window=50, long_window=200)
    
    return results

# computing strategy returns 
def compute_strategy_returns(df):
    """
    Computes the strategy's returns based on the position.
    """
    df["returns"] = df["price"].pct_change()
    df["strategy_returns"] = df["position"] * df["returns"]

    df["cumulative_market"] = (1 + df["returns"]).cumprod()
    df["cumulative_strategy"] = (1 + df["strategy_returns"]).cumprod()

    return df

def run_backtest(series):
    """
    Run a complete backtest on the given series using the best strategy.
    Returns both the backtest dataframe and performance metrics.
    """
    # Use the Standard strategy (50, 200) as default
    df_bt = sma_crossover(series, short_window=50, long_window=200)
    
    # Compute strategy returns
    df_bt = compute_strategy_returns(df_bt)
    
    # Compute performance metrics
    strategy_metrics = compute_performance_metrics(df_bt)
    
    return df_bt, strategy_metrics

# computing performance metrics
def compute_performance_metrics(df):
    strategy_returns = df["strategy_returns"].dropna()
    
    total_return = df["cumulative_strategy"].iloc[-1] - 1

    sharpe = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std()
    
    max_drawdown = (
        df["cumulative_strategy"] / 
        df["cumulative_strategy"].cummax() - 1
    ).min()

    win_rate = (strategy_returns > 0).mean()
    
    return {
        "total_return": float(total_return),
        "sharpe": float(sharpe),
        "max_drawdown": float(max_drawdown),
        "win_rate": float(win_rate)
    }
