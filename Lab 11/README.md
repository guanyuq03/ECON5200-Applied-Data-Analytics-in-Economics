# Data Wrangling & Engineering Pipeline

## Objective
Design and implement a structured preprocessing pipeline to transform a noisy human-resources economics dataset into a modeling-ready format through systematic feature engineering and statistically informed missing data imputation.

## Methodology
- **Data Audit & Missingness Mapping:**  
  Conducted an exploratory audit of the dataset (`messy_hr_economics.csv`) to identify structural inconsistencies, variable types, and patterns of missing data. Visual diagnostics were used to characterize missingness patterns consistent with *Missing At Random (MAR)* assumptions.

- **Missing Data Strategy:**  
  Implemented targeted imputation strategies based on variable structure and inferred missingness mechanisms, ensuring minimal distortion of underlying economic relationships.

- **Categorical Feature Engineering:**  
  Encoded categorical variables using statistically appropriate techniques to prepare them for econometric modeling while preserving interpretability.

- **Dummy Variable Trap Mitigation:**  
  Prevented perfect multicollinearity in categorical encodings by explicitly removing a reference category, ensuring stable coefficient estimation within regression frameworks.

- **High-Cardinality Feature Compression:**  
  Applied **Target Encoding** to compress high-cardinality geographic variables, reducing dimensionality while retaining predictive signal associated with regional economic variation.

- **Pipeline Implementation:**  
  The workflow was implemented using a Python-based data stack including `pandas` for transformation, `missingno` for missingness diagnostics, `category_encoders` for advanced encoding strategies, and `statsmodels` for econometric compatibility checks.

## Key Findings
- The dataset exhibited structured missingness patterns consistent with **Missing At Random (MAR)** rather than purely random absence.
- Properly handling categorical encodings avoided the **Dummy Variable Trap**, preventing perfect multicollinearity that would otherwise invalidate regression estimates.
- **Target Encoding** significantly reduced dimensionality from high-cardinality geographic variables while preserving economically relevant signal.
- The resulting engineered dataset is fully compatible with econometric modeling frameworks and suitable for downstream regression or causal analysis.
