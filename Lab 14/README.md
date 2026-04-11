# AI Capex Diagnostic Modeling

## Objective

To rigorously evaluate and correct structural weaknesses in an OLS regression model predicting AI software revenue, ensuring statistically reliable inference through robust econometric techniques.

## Methodology

* Constructed a baseline Ordinary Least Squares (OLS) model to estimate the relationship between AI capital expenditure and software revenue outcomes.
* Conducted diagnostic tests to identify violations of classical linear regression assumptions, focusing on heteroscedasticity and multicollinearity.
* Detected non-constant variance patterns across capital expenditure tiers using residual analysis and variance structure evaluation.
* Assessed multicollinearity among deployment-related predictors through correlation structure and stability of coefficient estimates.
* Applied HC3 heteroscedasticity-consistent robust standard errors to correct biased inference caused by heteroscedastic residuals.
* Re-estimated model significance and confidence intervals under the corrected covariance structure.
* Visualized residual dispersion and model diagnostics using statistical plotting tools to validate findings.

## Key Findings

The baseline OLS model exhibited severe heteroscedasticity, particularly at higher levels of AI capital expenditure, leading to downward-biased standard errors and overstated statistical significance. After applying HC3 robust standard errors, confidence intervals widened substantially, correcting false precision in the estimates. This adjustment revealed that several deployment-related variables previously deemed highly significant were, in fact, more modest in their explanatory power. The results underscore the necessity of robust inference techniques when modeling rapidly scaling capital investment environments, where variance instability can materially distort econometric conclusions.
