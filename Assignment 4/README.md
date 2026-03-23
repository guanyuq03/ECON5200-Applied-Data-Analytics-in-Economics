# ECON 5200 - Assignment 4

## The Predictive Architecture: Predictive Forensics and Causal Machine Learning

### 📌 Overview

This project builds a predictive pricing model for medical procedures using real-world data challenges. The goal is to design a statistically sound and reliable system while avoiding common pitfalls such as omitted variable bias, multicollinearity, missing data issues, and high-dimensional categorical variables.

The analysis follows a structured pipeline including causal reasoning, feature engineering, model estimation, and diagnostic testing.

---

### 📂 Dataset

Two datasets are used:

* **OmniCare_Clinical_Vitals.csv**
  Contains patient physiological variables (weight, height, blood pressure, etc.)

* **OmniCare_Telemetry_Data.csv**
  Contains patient telemetry, diagnosis codes, and procedure cost data

---

### ⚙️ Methods and Workflow

#### Phase 1: Causal Topology and Multicollinearity

* Identified omitted variable bias using a DAG (poverty as confounder)
* Calculated Variance Inflation Factor (VIF)
* Detected multicollinearity between BMI, weight, and height
* Removed BMI to stabilize the feature set

---

#### Phase 2: Missing Data and Feature Engineering

* Visualized missing data using `missingno`
* Identified missingness as **MNAR (Missing Not At Random)**
* Explained why mean imputation would bias results
* Applied **Target Encoding** to high-cardinality diagnosis codes (850 categories)

---

#### Phase 3: OLS Modeling and Diagnostics

* Merged datasets into a final analytical dataframe
* Built an OLS regression model using `statsmodels`
* Evaluated model performance using RMSE (~$335)
* Conducted residual diagnostics:

  * Found mild heteroscedasticity visually
* Interpreted financial and operational risks of prediction errors

---

#### Phase 4: AI-Assisted Statistical Testing

* Designed a P.R.I.M.E. prompt for AI-assisted coding
* Implemented **White’s Lagrange Multiplier Test**
* Found strong statistical evidence of heteroscedasticity (p-value ≪ 0.05)

---

### 📊 Key Findings

* The model suffers from heteroscedasticity, especially at higher cost levels
* Prediction error (~$335) is large relative to procedure cost (~$1,200)
* The model is less reliable for high-cost (surge pricing) scenarios
* Careful feature engineering (VIF filtering, encoding) significantly improved stability

---

### ⚠️ Limitations

* Presence of heteroscedasticity violates OLS assumptions
* RMSE remains high for real-world deployment
* Missing data is MNAR, which is difficult to fully correct
* Model may produce unstable predictions for high-cost procedures

---

### 🚀 Future Improvements

* Apply log transformation to stabilize variance
* Use robust standard errors
* Explore nonlinear or regularized models (e.g., Ridge/Lasso)
* Improve handling of MNAR missing data

---

### 🤖 AI Usage

AI (ChatGPT) was used as a coding assistant and conceptual guide. It helped:

* Structure statistical explanations
* Generate and refine model diagnostics

All analysis decisions, interpretations, and final outputs were verified and implemented by the author.
