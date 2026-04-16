## **Project Title**

**Causal ML — DML and Causal Forests for Policy Evaluation**

---

## **Objective**

Estimate the causal effect of 401(k) eligibility on household financial assets and evaluate treatment effect heterogeneity using modern causal machine learning methods.

---

## **Methodology**

* Diagnosed and corrected a broken manual Double Machine Learning (DML) implementation by fixing three key issues: data leakage in cross-fitting, missing treatment residualization, and incorrect estimation formula
* Verified the corrected DML approach on simulated data, successfully recovering the true ATE of 5.0
* Applied DoubleML with Random Forest models and 5-fold cross-fitting to estimate the average treatment effect (ATE) of 401(k) eligibility on net financial assets
* Conducted sensitivity analysis to evaluate robustness to unobserved confounding
* Implemented CausalForestDML (EconML) to estimate individual-level treatment effects (CATE)
* Compared subgroup DML (income quartiles) with Causal Forest results to assess differences in detecting treatment effect heterogeneity

---

## **Key Findings**

* 401(k) eligibility has a positive and statistically significant effect on net financial assets, with an estimated ATE of approximately $8,600
* Sensitivity analysis shows the result is reasonably robust, requiring a meaningful level of unobserved confounding to overturn the finding
* Treatment effects are highly heterogeneous across individuals, with some households experiencing much larger gains
* Higher-income households benefit substantially more from 401(k) eligibility, but there is still important variation within income groups
* Causal Forest provides a more detailed view of heterogeneity compared to subgroup DML, which can miss variation within predefined groups
