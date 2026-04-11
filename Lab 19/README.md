## Tree-Based Models — Random Forests

### Objective
Assess the predictive performance and interpretability of tree-based ensemble methods relative to linear benchmarks in modeling housing prices.

### Methodology
Used the California Housing dataset with 20,640 observations and 8 features  
Split data into training and test sets for out-of-sample evaluation  
Trained Decision Tree, Ridge Regression, and Random Forest models  
Tuned Random Forest using GridSearchCV over n_estimators, max_depth, and max_features  
Evaluated model performance using RMSE and R² on the test set  
Computed and compared feature importance using MDI and permutation methods  
Applied SHAP analysis to interpret individual predictions and global patterns  
Built a classification variant and compared Random Forest against logistic regression using AUC  
Developed an interactive dashboard with Plotly and ipywidgets to explore model behavior and feature importance  

### Key Findings
Random Forest achieved R² ≈ 0.81, significantly outperforming Ridge Regression (R² ≈ 0.58) and a single Decision Tree  
Hyperparameter tuning yielded incremental performance gains over the default Random Forest  
Gradient Boosting provided slightly higher accuracy, though with modest practical improvement  
Feature importance rankings were broadly consistent across methods for top variables, but diverged for mid-level features  
SHAP analysis confirmed that importance reflects predictive contribution rather than causal impact  
Model performance improved with more trees but showed diminishing returns beyond approximately 200 estimators  
Overall, ensemble tree methods delivered strong predictive accuracy while requiring careful interpretation for policy or causal conclusions  