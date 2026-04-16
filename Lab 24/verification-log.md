## Verification Log

### Overview
This log documents the key verification steps used to ensure that all causal estimation methods in this project are implemented correctly and produce reliable results.

---

### 1. Manual DML Debugging

- Fixed three issues in the original implementation:
  - Data leakage in cross-fitting  
  - Missing residualization of the treatment variable  
  - Incorrect formula for estimating the treatment effect  
- Verified correctness using simulated data  
- Result: Estimated ATE is close to the true value (5.0), confirming the implementation is correct  

---

### 2. DoubleML ATE Estimation (401(k) Data)

- Model: DoubleMLPLR with Random Forest nuisance learners and 5-fold cross-fitting  
- Result:
  - ATE ≈ $8,600  
  - Statistically significant (p < 0.05)  
- Interpretation: 401(k) eligibility has a positive effect on net financial assets  

---

### 3. Sensitivity Analysis

- Method: DoubleML sensitivity analysis with cf_y = 0.03 and cf_d = 0.03  
- Result:
  - Robustness value ≈ 6%  
- Interpretation: A moderate level of unobserved confounding would be required to overturn the result  

---

### 4. Causal Forest (CATE Estimation)

- Model: CausalForestDML with Random Forest models and 5-fold cross-fitting  
- Result:
  - Mean CATE ≈ $7,700 (close to DML ATE)  
  - Large variation across individuals  
- Interpretation: Treatment effects are heterogeneous, not constant  

---

### 5. Subgroup vs. Individual Heterogeneity

- Compared:
  - Subgroup DML (income quartiles)  
  - Causal Forest (individual-level CATE)  
- Findings:
  - Higher-income groups have larger average treatment effects  
  - However, there is still substantial variation within each income group  
- Conclusion: Subgroup DML is useful but too coarse; Causal Forest captures finer heterogeneity  

---

### Final Check

- All models run without errors  
- Results are consistent across methods  
- Key outputs match expected ranges from theory and reference solutions  
