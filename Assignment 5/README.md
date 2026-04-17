# Unsupervised Learning — Clustering & Dimensionality Reduction

## Objective
Build and diagnose a clustering pipeline for economic data, ensuring correct preprocessing, model specification, and interpretable visualization of country-level patterns.

## Methodology
- Diagnosed four major pipeline errors:
  - Missing feature standardization (scale dominance issue)
  - Incorrect K-Means parameter (`k` vs `n_clusters`)
  - PCA applied before scaling (invalid variance structure)
  - Missing `random_state` (non-reproducibility)
- Implemented corrected pipeline:
  - StandardScaler → KMeans → PCA visualization
- Applied clustering to World Development Indicators (WDI) data
- Evaluated clustering performance using:
  - Silhouette score
  - Cluster size distribution
- Compared dimensionality reduction methods:
  - PCA (linear projection)
  - UMAP (nonlinear structure preservation)
- Built reusable module `clustering_utils.py`:
  - `run_kmeans_pipeline()`
  - `evaluate_k_range()`
  - `plot_pca_clusters()`
- Extended analysis with:
  - Hierarchical clustering (Ward linkage)
  - Dendrogram visualization
  - Cross-method cluster comparison

## Key Findings
- Standardization is critical: without it, GDP per capita dominates distance calculations and distorts clusters :contentReference[oaicite:0]{index=0}  
- Correct pipeline (scale → cluster → reduce) produces balanced and interpretable clusters
- PCA on standardized data captures multi-feature variation instead of a single dominant variable
- K-Means and hierarchical clustering produce similar but not identical groupings
- UMAP provides clearer separation than PCA in more complex data structures
- WDI clustering shows moderate structure (silhouette ~0.15–0.40), reflecting real-world economic heterogeneity


## Tools & Libraries
- Python (pandas, numpy)
- scikit-learn (KMeans, StandardScaler, PCA, silhouette_score)
- matplotlib
- UMAP
- scipy (hierarchical clustering)

## Notes
This lab emphasizes diagnostic thinking: small preprocessing mistakes (especially scaling and ordering) can completely invalidate clustering results, even when the code runs without errors.
