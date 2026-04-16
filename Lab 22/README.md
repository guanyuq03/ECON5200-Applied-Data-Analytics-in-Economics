## Project Title  
**Unsupervised Learning — Clustering & Dimensionality Reduction**

---

## Objective  
Apply unsupervised learning techniques to identify meaningful structure in economic and behavioral data, with a focus on clustering accuracy and dimensionality reduction for visualization.

---

## Methodology  
- Diagnosed and corrected a flawed K-Means pipeline:
  - Added feature standardization
  - Fixed incorrect parameter usage (`k` → `n_clusters`)
  - Reordered PCA after scaling
  - Ensured reproducibility with `random_state`
- Built a clean pipeline: **StandardScaler → K-Means → PCA visualization**
- Applied clustering to synthetic customer behavior data to simulate real-world segmentation
- Compared **PCA (linear)** vs **UMAP (nonlinear)** for dimensionality reduction
- Evaluated clustering quality using **silhouette scores**
- Implemented reusable functions in `clustering_utils.py` for scalable analysis

---

## Key Findings  
- The optimal number of clusters was **K = 4**, consistent with the underlying data structure  
- **UMAP provided clearer visual separation** of clusters than PCA, especially in distinguishing customer segments  
- **PCA captured general structure**, but clusters overlapped due to its linear nature  
- **Agglomerative clustering slightly outperformed K-Means** (higher silhouette score), suggesting the data does not fully satisfy K-Means’ spherical cluster assumption  
- Proper preprocessing (especially standardization) is critical — without it, clustering results are dominated by high-scale features like GDP  
