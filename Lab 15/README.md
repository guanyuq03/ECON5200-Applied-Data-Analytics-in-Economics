# Forecasting Architecture and the Bias-Variance Tradeoff

## Objective

To rigorously evaluate the bias-variance tradeoff in predictive modeling by demonstrating how high-complexity polynomial regression can produce misleadingly low training error while introducing significant instability and risk in out-of-sample forecasts.

## Methodology

* Collected and structured quarterly financial data for NVIDIA spanning 2024–2026, focusing on total corporate revenue.
* Engineered polynomial features up to the 7th degree to intentionally increase model complexity.
* Trained a baseline linear regression model on the expanded feature set to induce overfitting.
* Measured in-sample performance using Mean Squared Error (MSE), confirming near-zero training error.
* Evaluated out-of-sample performance using K-Fold Cross-Validation to obtain a robust estimate of generalization error.
* Conducted forward extrapolation to simulate next-quarter forecasting and observe model behavior under real-world deployment conditions.
* Visualized model fit and instability using plotted regression curves to highlight variance-driven oscillations.

## Key Findings

The high-degree polynomial model achieved near-perfect in-sample accuracy but failed catastrophically when evaluated out-of-sample, producing erratic and economically implausible forecasts. Cross-validation revealed a substantial increase in true predictive error, exposing the model’s high variance and lack of generalization. These results demonstrate that minimizing training error alone is insufficient for reliable forecasting and underscore the necessity of regularization techniques to constrain model complexity, stabilize predictions, and reduce operational risk in econometric applications.
