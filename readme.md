# Introduction

The repository aims to provide three different applications of the concept of eigenvalues and eigenvectors, namely PageRank algorithm, Singular Value Decomposition (SVD) Principal Component Analysis (PCA), along with simulations.


# Installation
This repository employs Python [manim](https://pypi.org/project/manim/) package to render mathematical animations. Make sure you run the following to install the package.

```bash
pip install manim==0.19.0
```

Moreover, [NumPy](https://pypi.org/project/numpy/) is strictly applied to implement the afore-mentioned algorithms. At some steps of processing, [Pandas](https://pypi.org/project/pandas/) is also used.

```bash
pip install numpy pandas
```
You can also check requirements.txt to align your local environment with the repo.


# Usage

The following implements SVD algorithm on data.
```python
import numpy as np
import pandas as pd
from applications.SVD import SVD

df = pd.read_csv("./data/iris_data.csv")
X = df.values[:, :4]
svd = SVD(n_rank=2)
svd.fit(X)
X_reduced = svd.transform()
```

The following implements PCA algorithm on data.
```python
import pandas as pd
from applications.PCA import PCA

df = pd.read_csv("./data/iris_data.csv")
X = df.values[:, :4]
X_reduced, eigenvalues, eigenvectors = PCA(X, n_components=3)
```

You can simulate PageRank algorithm with the following code. It generates an animation in the path ./media/videos/1080p60/ShowPageRank.mp4. 

```python
from applications.PageRank import PageRank
from utils.animation import ShowPageRank
from manim import *

pagerank = PageRank(n_pages=7, n_fraction=0.6, filepath="./logs/logs.json")
links, scores = pagerank.run()
print("Algorithm run")

ShowPageRank().render(True)
```