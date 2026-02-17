# Hypothesis Testing & Causal Evidence Architecture

## Objective  
This project reframes causal inference from a problem of *point estimation* to one of *scientific falsification*. Rather than optimizing for increasingly complex estimators, the analysis operationalizes the scientific method to explicitly test—and attempt to reject—competing causal narratives. Using experimental and observational contrasts in the Lalonde (1986) job training data, the goal is to determine whether claims of treatment efficacy survive rigorous statistical scrutiny.

In short: the focus is not *“How large is the effect?”* but *“Can the null hypothesis still plausibly stand?”*

---

## Technical Approach  
The analysis implements a layered hypothesis-testing framework designed to stress-test causal claims under realistic data conditions:

- **Parametric Inference (Signal-to-Noise Evaluation)**  
  - Estimated the Average Treatment Effect (ATE) using Welch’s T-Test to accommodate unequal variances between treatment and control groups.  
  - Interpreted results through a signal-to-noise lens, emphasizing effect detectability rather than point-estimate magnitude.

- **Non-Parametric Validation (Distribution-Free Testing)**  
  - Conducted a 10,000-iteration permutation test to validate findings without relying on normality assumptions—critical for skewed earnings data.  
  - Used resampling-based inference to assess whether observed effects could plausibly arise under the null distribution.

- **Statistical Discipline**  
  - Explicitly controlled for Type I error risk by pre-specifying hypotheses and avoiding post-hoc thresholding.  
  - Treated statistical significance as a falsification criterion, not a discovery tool.

All analyses were implemented using industry-standard scientific computing tools (e.g., SciPy) to ensure reproducibility and methodological transparency.

---

## Key Findings  
The null hypothesis of no treatment effect was rejected via **statistical contradiction**. Across both parametric and non-parametric tests, the job training intervention produced a statistically significant increase in real earnings of approximately **$1,795**. The consistency of results across inference regimes strengthens the causal interpretation and reduces dependence on fragile modeling assumptions.

---

## Business Insight  
In production data systems, hypothesis testing functions as the **safety valve of the algorithmic economy**. As data volume grows, so does the risk of spurious correlations, narrative overfitting, and “data grubbing” masquerading as insight.

Rigorous falsification:
- Prevents shipping models that optimize noise rather than signal  
- Forces causal claims to survive adversarial testing  
- Creates institutional guardrails against overconfident decision-making  

For modern organizations, disciplined hypothesis testing is not academic overhead—it is risk management. It ensures that product decisions, policy changes, and algorithmic interventions are grounded in evidence that has *failed to be disproven*, not merely fit to historical data.

---

*This project demonstrates how classical statistical reasoning remains essential infrastructure for trustworthy data science in high-stakes environments.*
