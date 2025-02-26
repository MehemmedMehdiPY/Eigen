import numpy as np

def eigh(A):
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]
    return eigenvalues, eigenvectors

def eig(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]
    return eigenvalues, eigenvectors

if __name__ == "__main__":
    A = np.array([2, 5, 1, -5, 1, 5,1, 3,2,5, 4, 7, 2, 5, 2]).reshape(5, 3)
    B = A.dot(A.T)
    eigenvalues, eigenvectors = eig(B)
    print(eigenvalues)
    print(eigenvectors)
    print(eigenvalues.shape, eigenvectors.shape)