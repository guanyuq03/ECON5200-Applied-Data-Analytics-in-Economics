# High-Dimensional GDP Growth Forecasting with Regularized Regression

## Objective

Forecast 5-year average GDP per capita growth across 120+ countries using high-dimensional World Development Indicators data, while demonstrating and correcting for overfitting through regularized regression techniques.

## Methodology

* Collected 35+ World Development Indicators (WDI) spanning trade, macroeconomics, education, infrastructure, health, finance, natural resources, agriculture, and governance using the `wbgapi` API (2013–2019).
* Constructed a cross-country dataset and defined GDP per capita growth as the target variable.
* Split the data into training and test sets to enable out-of-sample evaluation.
* Standardized all predictors using `StandardScaler` to ensure comparability across variables.
* Estimated a baseline OLS regression model to illustrate overfitting in a high-dimensional setting.
* Applied Ridge and Lasso regression using `RidgeCV` and `LassoCV` with 5-fold cross-validation to select optimal regularization parameters.
* Visualized coefficient shrinkage and selection dynamics using the Lasso path.
* Compared model performance using training and test (R^2) and mean squared error (MSE).

## Key Findings

* The OLS model exhibited clear overfitting, with high in-sample (R^2) but poor (often negative) out-of-sample performance.
* Both Ridge and Lasso regularization substantially improved generalization by reducing variance and stabilizing coefficient estimates.
* Ridge performed best in terms of predictive accuracy, particularly in the presence of correlated development indicators.
* Lasso achieved comparable test performance while selecting a sparse subset of predictors, highlighting the distinction between **predictive redundancy** and true economic relevance.
* The results illustrate the bias–variance tradeoff and underscore the importance of regularization when working with high-dimensional macroeconomic data.
