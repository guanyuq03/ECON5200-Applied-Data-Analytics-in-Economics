# FedSpeak 2.0 — NLP Pipeline for Central Bank Communications

## Objective
Develop a robust NLP pipeline to analyze FOMC meeting minutes and evaluate how different text representations capture monetary policy signals and predict Fed rate decisions.

## Methodology
- Diagnosed and corrected a flawed NLP pipeline, including issues with tokenization, sentiment dictionary selection, and TF-IDF configuration  
- Implemented proper preprocessing using `nltk.word_tokenize`, stopword removal, and lemmatization  
- Replaced the generic Harvard GI sentiment dictionary with the domain-specific Loughran-McDonald dictionary for financial text  
- Optimized TF-IDF feature engineering using appropriate `min_df`, `max_df`, and inclusion of bigrams  
- Generated dense semantic representations using sentence-transformers (`all-MiniLM-L6-v2`)  
- Performed clustering analysis using K-Means on both TF-IDF and embedding-based representations, with dimensionality reduction for visualization  
- Evaluated predictive performance using an expanding-window (time-series) cross-validation framework with logistic regression  

## Key Findings
TF-IDF outperformed embedding-based representations in predicting Fed tightening periods, achieving a higher mean AUC (0.818 vs 0.721). While sentence-transformer embeddings produced slightly better cluster separation, their predictive performance was less stable across time. The results suggest that monetary policy shifts are closely tied to specific and recurring vocabulary patterns, which TF-IDF captures more directly than semantic embeddings.
