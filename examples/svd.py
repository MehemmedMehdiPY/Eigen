import numpy as np
import pandas as pd
from applications.SVD import SVD

df = pd.read_csv("./data/iris_data.csv")
X = df.values[:, :4]
print(X.shape)

svd = SVD(n_rank=2)
svd.fit(X)
X_reduced = svd.transform()
print(X_reduced.shape)
print(np.linalg.matrix_rank(X_reduced))
