# NY Fed Yield Curve Recession Model Replication

## Objective

Replicate the Federal Reserve Bank of New York’s yield curve–based recession probability model by estimating a logistic regression on FRED macroeconomic data to forecast NBER recessions 12 months ahead.

## Methodology

* Collected and processed macroeconomic time series from FRED, including the 10-Year minus 3-Month Treasury yield spread (T10Y3M) and the NBER recession indicator (USREC), spanning 1970 to present
* Resampled daily yield data to a monthly frequency and constructed a 12-month lag of the yield spread to align with forward recession prediction
* Implemented a Linear Probability Model (LPM) and a logistic regression model using Python (pandas, numpy, scikit-learn) to compare predictive behavior
* Evaluated model performance and interpretability, including extraction of odds ratios and estimation of 95% confidence intervals using both scikit-learn and statsmodels
* Generated a recession probability time series and visualized model outputs, including comparison against historical recession periods
* Applied time-series-aware validation techniques (e.g., TimeSeriesSplit) to maintain temporal consistency in model estimation

## Key Findings

* The Linear Probability Model produced invalid probability estimates (below 0 and above 1), demonstrating its limitations for binary outcome modeling in macroeconomic contexts
* The logistic regression model correctly constrained predicted probabilities within the [0, 1] interval and captured the nonlinear S-shaped relationship between the yield spread and recession risk
* The estimated odds ratio confirmed a strong inverse relationship between the yield curve slope and future recession probability, consistent with established empirical findings
* The model successfully reproduced the historical pattern of elevated recession risk preceding downturns, including during major recession episodes since 1970
* During the 2022–2024 yield curve inversion period, the model signaled elevated recession probability, highlighting a notable divergence between historical patterns and realized outcomes, and underscoring the presence of model uncertainty in atypical macroeconomic environments
