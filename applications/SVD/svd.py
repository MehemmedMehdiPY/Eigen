import numpy as np
import sys
sys.path.append("../../")
from utils.eigen import eigh

class SVD():
    """Singular Value Decomposition"""
    def __init__(self, n_rank: int = 2):
        self.n_rank = n_rank

    def get_U(self):
        """U matrix"""
        eigenvalues, eigenvectors = eigh(self.AAT)
        indices = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:, indices]
        return eigenvectors
    
    def get_VT(self):
        """Transposed V matrix"""
        eigenvalues, eigenvectors = eigh(self.ATA)
        indices = np.argsort(eigenvalues)[::-1]

        # Transposing the eigenvectors
        eigenvectors = eigenvectors[:, indices].T
        
        return eigenvectors

    def get_Sigma(self):
        """Sigma matrix"""
        shape = self.A.shape

        # Choosing the lowest dimensions for sigmas
        if shape[0] > shape[1]:
            # If m > n, then choose n dimension
            k = shape[1]
            A_symmetric = self.ATA
        else:
            # If m <= n, then choose m dimension
            k = shape[0]
            A_symmetric = self.AAT
        
        eigenvalues, eigenvectors = eigh(A_symmetric)
        indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[indices]
        sigmas = np.sqrt(eigenvalues)        
        
        # Constructing Sigma (singular values) matrix in shape of m x n
        Sigma = np.zeros(shape)
        Sigma[:k, :k] = np.diag(sigmas)

        return Sigma

    def fit(self, A):
        self.A = A
        self.AAT = A.dot(A.T)
        self.ATA = A.T.dot(A)

        self.U = self.get_U()
        self.VT = self.get_VT()
        self.Sigma = self.get_Sigma()
    
    def transform(self):
        U = self.U[:, :self.n_rank]
        Sigma = self.Sigma[:self.n_rank, :self.n_rank]
        VT = self.VT[:self.n_rank, :]
        return U.dot(Sigma).dot(VT)
    

if __name__ == "__main__":
    import pandas as pd
    X = pd.read_csv("../../data/iris_data.csv").values[:, :4]
    print(X.shape)
    
    svd = SVD(n_rank=2)
    svd.fit(X)
    B = svd.transform()
    print(B.shape)
    print(np.linalg.matrix_rank(B))
    