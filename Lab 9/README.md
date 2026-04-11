# Recovering Experimental Truths via Propensity Score Matching

## Objective
This project demonstrates how causal inference methods—specifically Propensity Score Matching—can correct severe selection bias in observational data and recover experimentally valid treatment effects where naive estimators fail.

## Methodology
- Modeled treatment assignment as a function of observed covariates to explicitly capture selection bias inherent in observational data.  
- Estimated individual propensity scores using logistic regression to summarize multidimensional covariate information into a single balancing metric.  
- Applied nearest-neighbor matching on the propensity score to construct a counterfactual control group comparable to treated units.  
- Evaluated treatment effects post-matching to assess bias reduction relative to naive observational estimates.

## Key Findings
- The naive difference-in-means estimator produced a highly misleading treatment effect of approximately **–$15,204**, reflecting substantial selection bias.  
- After applying Propensity Score Matching, the estimated treatment effect converged to approximately **+$1,800**, closely aligning with the known experimental benchmark.  
- The results empirically validate Propensity Score Matching as an effective tool for recovering causal effects from non-randomized data when assumptions are carefully implemented.
