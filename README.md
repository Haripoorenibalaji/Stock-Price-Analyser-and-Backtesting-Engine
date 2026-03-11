**LLM-Assisted Stock Analysis & Strategy Backtesting Engine**

A modular Python system that combines time-series analysis, algorithmic trading backtesting, and LLM-based explainability to evaluate stocks and generate interpretable trading decisions.

The project analyzes historical stock data, evaluates trading strategies, computes quantitative risk metrics, and uses a large language model to explain the resulting BUY / HOLD / AVOID decision.

**Overview**

This project implements a multi-layer financial analysis pipeline:

Time-series analysis
Strategy backtesting
Quantitative decision engine
LLM-generated explanation

The goal is to create a system where:
    numbers determine decisions
    LLMs explain the reasoning

This ensures the system remains deterministic, reproducible, and interpretable.

**System Architecture**

Pipeline:
    dataset → preprocessing → analysis → insights → backtesting → decision → LLM explanation

Detailed workflow:

User selects stock
        ↓
main.py
        ↓
dataset.py
        ↓
preprocessing.py
        ↓
analysis.py
        ↓
insights.py
        ↓
backtesting.py
        ↓
decision.py
        ↓
llm_explainer.py
        ↓
Final report + explanation

**Features**

1. Time-Series Analysis
   -Trend detection
   -Volatility measurement
   -Seasonality detection
   -Anomaly identification

2. Strategy Backtesting
   -SMA crossover trading strategy
   -Position simulation
   -Strategy vs market performance comparison

3. Performance Metrics
   -Total return
   -Sharpe ratio
   -Maximum drawdown
   -Win rate

4. Decision Engine
   -Computes a weighted score based on
   -Trend strength
   -Volatility
   -Strategy performance
   -Risk metrics

**Outputs**

BUY
HOLD
AVOID

**LLM Explainability**

A large language model generates a natural-language explanation of the decision using only computed metrics.

This provides interpretable financial insights for non-technical users.

**Project Structure**

stock-price-analyser
│
├── src/
│   ├── analysis.py        # time-series analysis
│   ├── backtesting.py     # strategy engine
│   ├── dataset.py         # data loading
│   ├── preprocessing.py   # data cleaning
│   ├── insights.py        # structured market insights
│   ├── decision.py        # BUY/HOLD/AVOID logic
│   ├── llm_explainer.py   # LLM explanation layer
│   ├── main.py            # pipeline orchestrator
│   └── colorsetup.py      # visualization settings
│
├──Final-50-stocks.csv
├── requirements.txt
├── README.md
└── .gitignore

**Installation**

1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/stock-price-analyser.git
cd stock-price-analyser

2. Install dependencies:

pip install -r requirements.txt

**Running the Project**

Run the full analysis pipeline:

python src/main.py

**Example output**

Running full analysis for TATASTEEL...

=== FINAL REPORT ===

Trend: upward
Volatility: moderate
Sharpe ratio: 0.77
Max drawdown: -68%

Decision: HOLD
Score: 0.65

LLM Explanation:

The HOLD decision is supported by a moderate upward trend but elevated volatility,
a relatively low win rate, and a large maximum drawdown. While the strategy is
profitable overall, the risk-adjusted return remains moderate.

**Technologies Used**

1. Python
2. NumPy
3. Pandas
4. Matplotlib
5. Seaborn
6. Statsmodels
7. OpenRouter / OpenAI API

**Future Improvements**

Potential extensions:
     1. Additional trading strategies (RSI, MACD, momentum)
     2. Portfolio optimization
     3. Transaction cost modeling
     4. Walk-forward validation
     5. FastAPI backend
     6. React dashboard
     7. ML-based trading signals

**Key Learning Outcomes**

This project demonstrates:
   - financial time-series analysis
   - algorithmic trading strategy evaluation
   - modular system design
   - explainable AI workflows
   - integration of LLMs with quantitative models

**License**

MIT License
