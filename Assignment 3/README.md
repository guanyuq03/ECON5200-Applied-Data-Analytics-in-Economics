# Econ 5200 – Assignment 3  
## The Causal Architecture: Bootstrapping, Permutation, and Selection Bias
---

## Overview

This assignment applies computational methods to isolate causal effects in non-ideal real-world settings. Instead of relying on fragile parametric assumptions, we use non-parametric resampling, permutation testing, and propensity score matching to separate correlation from causation.

The assignment is structured in four phases:

1. Bootstrapping non-parametric uncertainty  
2. Permutation testing in A/B experiments  
3. Propensity Score Matching (PSM) to mitigate selection bias  
4. Love Plot visualization to evaluate covariate balance  

---

# Phase 1: Bootstrapping Non-Parametric Uncertainty

Simulate a zero-inflated and right-skewed tip distribution:

- 100 zero tips  
- 150 exponential tips (scale = 5.0)

A manual bootstrap procedure (10,000 resamples) is implemented to estimate the sampling distribution of the median.

### Key Result

- Bootstrap Median ≈ 0.76  
- 95% CI ≈ [0.27, 1.36]

The confidence interval is asymmetric due to the heavy right tail and mass at zero. This demonstrates why normal-based confidence intervals are unreliable in skewed distributions.

---

# Phase 2: Non-Parametric Permutation Test

Simulate an A/B test of a routing algorithm:

- Control: Normal(35, 5)  
- Treatment: Log-Normal(mean=3.4, sigma=0.4)

Observed difference in means (Control − Treatment):

≈ 2.26 minutes

A manual permutation test (5,000 iterations) is performed to compute the empirical p-value.

### Key Result

Empirical p-value ≈ 0.0004  
(2 out of 5,000 permutations were as extreme as observed)

This confirms statistical significance without relying on normality or homoscedasticity assumptions.

---

# Phase 3: Propensity Score Matching (PSM)

The SwiftPass loyalty program analysis investigates selection bias.

Naive Simple Difference in Means (SDO):

Subscribers − Non-subscribers ≈ 17.57

However, high-spending users self-select into the program.

Using Logistic Regression to estimate propensity scores and Nearest Neighbor matching (1-to-1), we compute:

Average Treatment Effect on the Treated (ATT):

≈ 9.91

The reduction from 17.57 to 9.91 indicates that the naive estimate was upward biased due to selection effects.

---

# Phase 4: Love Plot Visualization

A Love Plot (Standardized Mean Differences) evaluates covariate balance before and after matching.

### Before Matching
- pre_spend SMD ≈ 0.67  
- account_age SMD ≈ 0.32  
- support_tickets SMD ≈ 0.17  

Severe imbalance is present.

### After Matching
All SMD values < 0.02

This visual evidence strongly suggests that matching successfully mitigated selection bias on observed covariates.

However, balance on observed variables does not guarantee elimination of unobserved confounding.

---

# Methods Used

- Manual Bootstrap (no built-in shortcuts)
- Manual Permutation Test
- Logistic Regression (Propensity Score)
- Nearest Neighbor Matching
- Standardized Mean Differences (SMD)
- Seaborn & Matplotlib Visualization

All methods were implemented explicitly to demonstrate understanding of the underlying causal mechanics.

---

# Key Takeaways

1. Parametric assumptions can fail in skewed and zero-inflated data.  
2. Permutation tests provide exact empirical inference.  
3. Naive observational differences can severely overstate causal effects.  
4. Propensity Score Matching reduces selection bias in observed covariates.  
5. Love Plots provide visual diagnostic evidence of balance improvement.

---
