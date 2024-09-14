# Import necessary libraries
import yfinance as yf
import riskfolio as rf
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Configure pandas and warnings
pd.options.display.float_format = "{:.4%}".format
warnings.filterwarnings("ignore")

# Define stock tickers and factor ETFs for the analysis
stock_list = ["AMZN", "AAPL", "NVDA", "META", "TSLA", "MSFT", "GOOG"]
factor_etfs = ["MTUM", "QUAL", "VLUE", "SIZE", "USMV"]

# Set the date range for fetching historical data
start_date = "2020-01-01"
end_date = "2024-07-31"

# Download adjusted close price data for stocks and factor ETFs
stock_data = (
    yf.download(stock_list, start=start_date, end=end_date)["Adj Close"]
    .pct_change()
    .dropna()
)

factor_data = (
    yf.download(factor_etfs, start=start_date, end=end_date)["Adj Close"]
    .pct_change()
    .dropna()
)

# Initialize the Riskfolio portfolio optimization model
portfolio = rf.Portfolio(returns=stock_data)

# Compute asset statistics using historical returns and Ledoit-Wolf shrinkage
portfolio.assets_stats(method_mu="hist", method_cov="ledoit")

# Define a constraint for the minimum acceptable return
portfolio.lower_return_bound = 0.00056488 * 1.5

# Perform Principal Component Regression to determine factor loadings
factor_loadings = rf.loadings_matrix(
    X=factor_data,
    Y=stock_data, 
    feature_selection="PCR",
    n_components=0.95
)

# Display factor loadings using a heatmap
factor_loadings.style.format("{:.4f}").background_gradient(cmap='RdYlGn')

# Set factor statistics for portfolio optimization
portfolio.factors = factor_data
portfolio.factors_stats(
    method_mu="hist",
    method_cov="ledoit",
    feature_selection="PCR",
    n_components=0.95
)

# Optimize the portfolio to maximize the Sharpe ratio
optimal_weights = portfolio.optimization(
    model="FM",  # Factor Model
    rm="MV",     # Mean-Variance
    obj="Sharpe",  # Objective to maximize Sharpe Ratio
    hist=False
)

# Plot a pie chart of the optimized asset weights
ax = rf.plot_pie(
    w=optimal_weights,
    title='Optimal Portfolio Allocation',
    others=0.05,
    nrow=25,
    cmap="tab20"
)

# Display the pie chart
plt.show()
