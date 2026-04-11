# Fraud Detection Model Evaluation — Metrics that Matter

## Objective

Evaluate the performance of a logistic regression–based fraud detection model on a highly imbalanced dataset, emphasizing decision-relevant metrics beyond accuracy to better reflect real-world operational and economic trade-offs.

## Methodology

* Utilized the Kaggle Credit Card Fraud Detection dataset consisting of 284,807 anonymized European transactions, including PCA-transformed features (V1–V28), transaction amount, and a binary fraud label.
* Established a naive baseline classifier to illustrate the limitations of accuracy in the presence of extreme class imbalance (0.172% fraud rate).
* Trained a logistic regression model using scikit-learn to estimate fraud probabilities.
* Evaluated model performance using confusion matrices and classification reports, focusing on Precision, Recall, and F1-Score for the minority (fraud) class.
* Constructed ROC curves and computed ROC-AUC to assess ranking performance across thresholds.
* Generated Precision-Recall curves and PR-AUC to better capture performance under class imbalance.
* Performed threshold analysis to identify the F1-optimal decision boundary and compare it against the default 0.5 cutoff.
* Incorporated a business constraint (maximum of 500 daily investigations) to select an operational threshold aligned with real-world resource limitations.

## Key Findings

* Demonstrated the accuracy paradox: a naive classifier achieved 99.83% accuracy while failing to detect any fraudulent transactions (zero recall).
* Logistic regression substantially improved discriminatory power, achieving strong ROC-AUC and meaningful PR-AUC, indicating effective ranking of fraudulent transactions despite severe imbalance.
* The optimal classification threshold differed significantly from the default 0.5, highlighting the importance of threshold tuning in imbalanced settings.
* Under a fixed investigation capacity, the model enabled a more economically relevant operating point, prioritizing high-risk transactions while managing false positives.
* Results underscore that evaluation metrics must align with decision objectives, particularly in fraud detection contexts where class imbalance and asymmetric costs are central.
