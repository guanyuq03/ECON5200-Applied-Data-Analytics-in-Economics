# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective

To empirically demonstrate how multivariate regression isolates causal relationships in housing markets by applying a hedonic pricing model and manually verifying the Frisch–Waugh–Lovell (FWL) theorem using synthetic California real estate data.

## Methodology

* **Data Source:** Zillow-style synthetic dataset representing 2026 California housing metrics, including `Sale_Price`, `Property_Age`, and `Distance_to_Tech_Hub`.
* **Baseline Multivariate Model:** Estimated a multivariate hedonic pricing regression using Ordinary Least Squares (OLS) to quantify the marginal effect of property characteristics on housing prices.
* **Omitted Variable Bias Demonstration:** Constructed a reduced model excluding `Distance_to_Tech_Hub` to illustrate how omitted spatial productivity factors distort coefficient estimates.
* **Residual Extraction (FWL Step 1):** Regressed `Property_Age` on `Distance_to_Tech_Hub` and extracted the resulting residuals to isolate the component of property age orthogonal to tech-hub proximity.
* **Outcome Residualization (FWL Step 2):** Regressed `Sale_Price` on `Distance_to_Tech_Hub` and extracted residuals representing price variation independent of proximity effects.
* **Partial Regression (FWL Step 3):** Regressed the residualized price on the residualized property age, effectively partialling out the shared covariance with the omitted variable.
* **Coefficient Verification:** Compared the coefficient from the partial regression to the corresponding coefficient in the full multivariate model to confirm the Frisch–Waugh–Lovell theorem.

## Key Findings

The reduced model exhibited clear **omitted variable bias**, where failing to control for proximity to major technology employment hubs incorrectly attributed price variation to the physical age of the property. This distortion arose because `Property_Age` and `Distance_to_Tech_Hub` share systematic covariance in urban housing markets. By manually applying the **Frisch–Waugh–Lovell theorem**, the analysis isolated the orthogonal component of each variable through residualization, eliminating the confounding influence. The resulting partial regression produced a coefficient that matched the multivariate OLS estimate exactly, providing a direct computational proof of the theorem and demonstrating how regression algorithms enforce **ceteris paribus** conditions in high-dimensional econometric models.
