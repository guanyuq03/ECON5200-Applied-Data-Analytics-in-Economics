"""
Simple SHAP analysis tools.

Functions:
- explain_prediction: show SHAP waterfall for one row
- global_importance: show SHAP beeswarm plot
- compare_importance: compare MDI vs SHAP importance
"""

from typing import Any, Tuple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def explain_prediction(model: Any, X: pd.DataFrame, idx: int) -> plt.Figure:
    """
    Show SHAP waterfall plot for one observation.
    """
    import shap

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    explanation = shap.Explanation(
        values=shap_values[idx],
        base_values=explainer.expected_value,
        data=X.iloc[idx],
        feature_names=X.columns
    )

    plt.figure()
    shap.plots.waterfall(explanation, show=False)
    return plt.gcf()


def global_importance(model: Any, X: pd.DataFrame) -> plt.Figure:
    """
    Show SHAP beeswarm plot (global importance).
    """
    import shap

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    explanation = shap.Explanation(
        values=shap_values,
        base_values=explainer.expected_value,
        data=X,
        feature_names=X.columns
    )

    plt.figure()
    shap.plots.beeswarm(explanation, show=False)
    return plt.gcf()


def compare_importance(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series
) -> Tuple[pd.Series, pd.Series, plt.Figure]:
    """
    Compare MDI importance vs SHAP importance.
    """
    import shap

    # MDI
    mdi = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    # SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    shap_imp = pd.Series(
        np.abs(shap_values).mean(axis=0),
        index=X.columns
    ).sort_values(ascending=False)

    # plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    mdi.sort_values().plot.barh(ax=axes[0])
    axes[0].set_title("MDI")

    shap_imp.sort_values().plot.barh(ax=axes[1])
    axes[1].set_title("SHAP")

    plt.tight_layout()

    return mdi, shap_imp, fig