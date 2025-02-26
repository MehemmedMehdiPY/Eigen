import numpy as np
import sys
sys.path.append("../../")
from utils.preprocessing import standard_scale

def PCA(X, n_components: int = 2):
    # Scaling 
    X_scaled = standard_scale(X)

    # Covariance matrix
    cov_matrix = np.cov(X_scaled.T)

    # Obtaining eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sorting eigenvalues and eigenvectors in a descending order
    indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]

    # Choosing eigenvectors
    eigenvectors_reduced = eigenvectors[:, :n_components]

    # Obtaining the decomposed matrix
    X_reduced = X_scaled.dot(eigenvectors_reduced)

    return X_reduced, eigenvalues, eigenvectors

if __name__ == "__main__":
    from sklearn.datasets import load_iris

    data = load_iris()
    X = data["data"]
    X_scaled = (X - X.mean(axis=0)) / X.std(axis=0)
    
    X, eigenvalues, eigenvectors = PCA(X, n_components=2)
    print(X.shape, eigenvalues.shape, eigenvectors.shape)
 