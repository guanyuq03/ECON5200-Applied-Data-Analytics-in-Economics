"""
clustering_utils.py — Reusable Clustering Pipeline Module

Functions for standardized K-Means clustering, K evaluation,
and PCA visualization.

Author: Guanyu Qu
Course: ECON 5200, Lab 22
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from typing import List, Dict


def run_kmeans_pipeline(
    df: pd.DataFrame,
    features: List[str],
    k: int,
    random_state: int = 42
) -> Dict:
    """End-to-end K-Means pipeline."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        n_init='auto',
        random_state=random_state
    )
    labels = kmeans.fit_predict(X_scaled)
    sil = silhouette_score(X_scaled, labels)

    return {
        'labels': labels,
        'scaler': scaler,
        'model': kmeans,
        'X_scaled': X_scaled,
        'silhouette': sil,
        'inertia': kmeans.inertia_
    }


def evaluate_k_range(
    X: np.ndarray,
    k_range: range,
    random_state: int = 42
) -> pd.DataFrame:
    """Evaluate clustering quality across a range of K values."""
    results = []
    for k in k_range:
        km = KMeans(n_clusters=k, init='k-means++',
                    n_init='auto', random_state=random_state)
        labels = km.fit_predict(X)
        results.append({
            'k': k,
            'wcss': km.inertia_,
            'silhouette': silhouette_score(X, labels)
        })
    return pd.DataFrame(results)


def plot_pca_clusters(
    X: np.ndarray,
    labels: np.ndarray,
    feature_names: List[str]
) -> None:
    """PCA 2D scatter plot with cluster coloring."""
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    fig, ax = plt.subplots(figsize=(10, 7))
    scatter = ax.scatter(
        X_pca[:, 0], X_pca[:, 1],
        c=labels, cmap='Set1',
        alpha=0.7, edgecolors='white', s=60
    )
    ax.set_xlabel(
        f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)',
        fontsize=12
    )
    ax.set_ylabel(
        f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)',
        fontsize=12
    )
    ax.set_title('K-Means Clusters (PCA Projection)', fontsize=13)
    plt.colorbar(scatter, label='Cluster')
    plt.tight_layout()
    plt.show()

    # Print top PC1 loadings
    loadings = pd.Series(pca.components_[0], index=feature_names)
    print('Top PC1 loadings:')
    for feat in loadings.abs().nlargest(3).index:
        print(f'  {feat}: {loadings[feat]:.4f}')
