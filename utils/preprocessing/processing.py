def standard_scale(X):
    return (X - X.mean(axis=0)) / X.std(axis=0)


if __name__ == "__main__":
    import numpy as np
    X = np.array([[1, 4], [0, 2]])
    X = standard_scale(X)
    print(X)