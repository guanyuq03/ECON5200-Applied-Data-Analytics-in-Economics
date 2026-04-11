# Architecting the Prediction Engine

## Objective
Design and implement a multivariate econometric prediction engine capable of forecasting residential real estate valuations and evaluating model performance through out-of-sample error measurement.

## Methodology
- Utilized the **Zillow ZHVI 2026 Micro Dataset**, a cross-sectional dataset representing modern U.S. residential real estate market characteristics.
- Implemented the analytical workflow in **Python**, using **pandas** and **numpy** for data handling and numerical operations.
- Specified a **multivariate Ordinary Least Squares (OLS) hedonic pricing model** using the **statsmodels Patsy Formula API** to model housing values as a function of structural and locational attributes.
- Estimated the regression model to capture the marginal contribution of each property characteristic to home valuation.
- Generated in-sample predictions from the fitted model to transition from classical explanatory econometrics toward predictive modeling.
- Evaluated predictive accuracy using **Root Mean Squared Error (RMSE)**, measuring the average magnitude of prediction error directly in U.S. dollar terms.

## Key Findings
The analysis successfully operationalized a hedonic pricing framework as a predictive engine rather than solely an explanatory econometric model. By computing the **RMSE in actual dollar units**, the model’s predictive performance can be interpreted in economically meaningful terms, providing a clear estimate of the algorithm’s financial error margin. This metric enables direct assessment of **model risk in a real-estate valuation context**, translating statistical performance into practical business insight regarding the expected magnitude of valuation deviations.
