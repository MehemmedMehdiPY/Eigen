import pandas as pd
from applications.PCA import PCA

df = pd.read_csv("./data/iris_data.csv")
X = df.values[:, :4]
print(X.shape)

print(df.corr())
X_reduced, eigenvalues, eigenvectors = PCA(X, n_components=3)
X_reduced_df = pd.DataFrame(X_reduced)

print(X_reduced.shape)
print(X_reduced_df.corr().round(3))
