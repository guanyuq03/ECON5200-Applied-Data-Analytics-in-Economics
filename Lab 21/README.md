## Project Title
Time Series Forecasting — ARIMA, GARCH & Bootstrap

## Objective
Develop a robust and diagnostically sound time series forecasting pipeline that integrates ARIMA-based models, volatility modeling, and distribution-free uncertainty quantification for macroeconomic and financial data.

## Methodology
- Diagnosed a misspecified ARIMA pipeline by identifying non-stationarity (d=0 on trending CPI), omitted seasonality, and missing residual diagnostics.
- Corrected the specification using a SARIMA framework with appropriate differencing and seasonal terms for monthly CPI data.
- Evaluated model adequacy through residual diagnostics, including the Ljung-Box test for autocorrelation.
- Modeled financial market volatility using a GARCH(1,1) process applied to S&P 500 daily log returns.
- Quantified forecast uncertainty using both parametric confidence intervals and block bootstrap methods to account for non-Gaussian residual behavior.
- Built a reusable evaluation module with functions for Mean Absolute Scaled Error (MASE) and expanding-window backtesting to assess forecast performance.

## Key Findings
- The corrected SARIMA model successfully addressed non-stationarity and incorporated seasonal structure, but residual diagnostics indicate remaining autocorrelation, suggesting the model is not fully specified.
- GARCH(1,1) results show strong volatility persistence, with **α + β ≈ 0.9829**, implying a slow decay of volatility shocks.
- The estimated half-life of volatility shocks is approximately **40 days**, indicating that periods of elevated market uncertainty persist over several weeks.
- Block bootstrap forecast intervals are generally wider than parametric SARIMA intervals, reflecting additional uncertainty from non-normal residuals and providing a more realistic measure of forecast risk.
