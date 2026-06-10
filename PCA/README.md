# PCA from Scratch: Understanding Dimensionality Reduction

A clean, educational implementation of Principal Component Analysis (PCA) using only NumPy, with full validation against `scikit-learn`. Includes synthetic 2D visualisations (centering, eigenvectors, projections, reconstruction) and a real‑world example on the Iris dataset.

## 🔍 What This Project Demonstrates

- **Manual implementation** of PCA: centering, covariance matrix, eigen‑decomposition, projection, and reconstruction.
- **sklearn‑compatible API** (`fit`, `transform`, `fit_transform`, `inverse_transform`).
- **Validation** – compares results with `sklearn.decomposition.PCA` to ensure correctness.
- **Rich visualisations**:
  - Centered data cloud with eigenvectors scaled by √eigenvalue.
  - Orthogonal projection onto the first principal component.
  - Reconstruction from 1 component vs original (with error segments).
  - Scree plot + cumulative explained variance.
  - Reconstruction error (MSE) as a function of number of components.
- **Real dataset** – Iris (4D reduced to 2D) with colour‑coded species.