import numpy as np

A = np.array([3, 7,2 , 8, 2, 4, 6, 2, 6, 1, 2, 4, 5, 1, 5]).reshape(5, 3)
print(A)
print(A.shape)
AU = A.dot(A.T)
AV = A.T.dot(A)

print(AV.shape)

values_V, vectors_V = np.linalg.eig(AV)
values_U, vectors_U = np.linalg.eig(AU)
indices = np.argsort(values_V)[::-1]
values_V = values_V[indices]
vectors_V = vectors_V[:, indices]

diagonal = np.diag(values_V ** .5)
sigma = np.zeros(A.shape)
sigma[:diagonal.shape[0], :diagonal.shape[1]] = diagonal
print(sigma)

print(vectors_U.shape, sigma.shape, vectors_V.shape)
print(vectors_U.dot(sigma).dot(vectors_V.T))