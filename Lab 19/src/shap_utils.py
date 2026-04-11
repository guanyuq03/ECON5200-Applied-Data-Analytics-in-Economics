from __future__ import annotations

from typing import Any, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def _check_dataframe(X: pd.DataFrame) -> None:
    """Check X is a pandas DataFrame."""
    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")


def _check_model_fitted(model: Any) -> None:
    """Basic check that model looks fitted."""
    if not hasattr(model, "predict"):
        raise ValueError("Model must have a predict method.")


def explain_prediction(model: Any, X: pd.DataFrame, idx: int) -> plt.Figure:
    """
    Make a SHAP waterfall plot for one row.

    Parameters
    ----------
    model : Any
        Fitted tree model.
    X : pd.DataFrame
        Feature data.
    idx : int
        Row number to explain.

    Returns
    -------
    plt.Figure
        Matplotlib figure.
    """
    import shap

    _check_dataframe(X)
    _check_model_fitted(model)

    if idx < 0 or idx >= len(X):
        raise IndexError("idx is out of range.")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    explanation = shap.Explanation(
        values=shap_values[idx],
        base_values=explainer.expected_value,
        data=X.iloc[idx],
        feature_names=X.columns.tolist(),
    )

    plt.figure()
    shap.plots.waterfall(explanation, show=False)
    return plt.gcf()


def global_importance(model: Any, X: pd.DataFrame) -> plt.Figure:
    """
    Make a SHAP beeswarm plot.

    Parameters
    ----------
    model : Any
        Fitted tree model.
    X : pd.DataFrame
        Feature data.

    Returns
    -------
    plt.Figure
        Matplotlib figure.
    """
    import shap

    _check_dataframe(X)
    _check_model_fitted(model)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    explanation = shap.Explanation(
        values=shap_values,
        base_values=np.repeat(explainer.expected_value, len(X)),
        data=X,
        feature_names=X.columns.tolist(),
    )

    plt.figure()
    shap.plots.beeswarm(explanation, show=False)
    return plt.gcf()


def compare_importance(
    model: Any,
    X: pd.DataFrame,
    y: pd.Series | np.ndarray,
) -> Tuple[pd.Series, pd.Series, plt.Figure]:
    """
    Compare MDI and SHAP importance.

    Parameters
    ----------
    model : Any
        Fitted tree model with feature_importances_.
    X : pd.DataFrame
        Feature data.
    y : pd.Series | np.ndarray
        Target values. Included for API consistency.

    Returns
    -------
    tuple
        mdi importance, shap importance, figure
    """
    import shap

    _check_dataframe(X)
    _check_model_fitted(model)

    if not hasattr(model, "feature_importances_"):
        raise ValueError("Model must have feature_importances_ for MDI comparison.")

    _ = y

    mdi = pd.Series(
        model.feature_importances_,
        index=X.columns,
        name="MDI",
    ).sort_values(ascending=False)

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X, check_additivity=False)

    shap_imp = pd.Series(
        np.abs(shap_values).mean(axis=0),
        index=X.columns,
        name="SHAP",
    ).sort_values(ascending=False)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    mdi.sort_values().plot.barh(ax=axes[0])
    axes[0].set_title("MDI Importance")
    axes[0].set_xlabel("Importance")

    shap_imp.sort_values().plot.barh(ax=axes[1])
    axes[1].set_title("SHAP Importance")
    axes[1].set_xlabel("Mean |SHAP|")

    plt.tight_layout()
    return mdi, shap_imp, fig