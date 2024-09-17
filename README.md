# Portfolio Optimization Using Principal Component Regression (PCR)

This project implements a portfolio optimization model using Python, focusing on maximizing the Sharpe ratio through Principal Component Regression (PCR) and factor analysis. It aims to optimize the asset allocation in a portfolio by considering various risk factors such as momentum, value, size, and volatility.

## Project Overview

The project covers:
- **Data Loading**: Fetching and preprocessing historical financial data for a set of stocks and factor ETFs.
- **Portfolio Optimization**: Using Riskfolio-lib to set up a portfolio optimization model.
- **Principal Component Regression**: Applying PCR to identify and analyze key factors affecting asset returns.
- **Sharpe Ratio Maximization**: Optimizing portfolio weights to maximize the Sharpe ratio, a measure of risk-adjusted return.
- **Visualization**: Displaying the optimized portfolio weights using a pie chart.

![Alt text](https://github.com/digantk31/Portfolio-Optimization-Using-PCA/blob/main/Optimal%20Portfolio%20Allocation.png)

## Features

- **Stock List**: Analyzes the top 7 stocks—Amazon (AMZN), Apple (AAPL), Nvidia (NVDA), Meta (META), Tesla (TSLA), Microsoft (MSFT), and Google (GOOG).
- **Factor ETFs**: Includes momentum (MTUM), quality (QUAL), value (VLUE), size (SIZE), and minimum volatility (USMV).
- **Optimization Techniques**: Utilizes historical data and Ledoit-Wolf shrinkage for stable optimization.
- **Output Visualization**: Pie chart representation of the optimized asset allocation.

## Libraries Used

- `yfinance` – For downloading historical financial data.
- `riskfolio-lib` – For portfolio optimization and factor analysis.
- `pandas` – For data manipulation and analysis.
- `matplotlib` – For plotting and visualization.

## Installation

To set up the project, clone the repository and install the required libraries:

```bash
git clone https://github.com/digantk31/Portfolio-Optimization-Using-PCA.git
cd Portfolio-Optimization-Using-PCA
pip install -r requirements.txt
```

## Acknowledgments

This project is inspired by and adapted from content in the [PyQuant News](https://www.pyquantnews.com/the-pyquant-newsletter/maximize-sharpe-with-powerful-optimization) newsletter on Maximize your Sharpe with a powerful optimization.
