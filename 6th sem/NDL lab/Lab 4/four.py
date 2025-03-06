
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.linear_model import Ridge

class RBFNetwork:
    def _init_(self, n_centers, regularization=0.0):
        self.n_centers = n_centers
        self.regularization = regularization

    def _rbf(self, x, center, sigma):
        return np.exp(-np.linalg.norm(x-center)*2 / (2*sigma*2))

    def _calculate_interpolation_matrix(self, X):
        G = np.zeros((X.shape[0], self.n_centers))
        for i, x in enumerate(X):
            for j, center in enumerate(self.centers):
                G[i, j] = self._rbf(x, center, self.sigma)
        return G

    def fit(self, X, y):
        kmeans = KMeans(n_clusters=self.n_centers, random_state=0).fit(X)
        self.centers = kmeans.cluster_centers_
        self.sigma = np.mean(cdist(X, self.centers, 'euclidean'))
        G = self._calculate_interpolation_matrix(X)
        self.regressor = Ridge(alpha=self.regularization)
        self.regressor.fit(G, y)

    def predict(self, X):
        G = self._calculate_interpolation_matrix(X)
        return self.regressor.predict(G)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Training and evaluating RBF network
for reg in [0.0, 0.1, 1.0, 10.0]:
    rbf_net = RBFNetwork(n_centers=2, regularization=reg)
    rbf_net.fit(X, y)
    predictions = rbf_net.predict(X)
    print(f'Regularization: {reg}')
    print(f'Predictions: {predictions}')
    print(f'Error: {np.mean((predictions - y) ** 2)}\n')


'''
output
Regularization: 0.0
Predictions: [-1.16328552e-16  1.00000000e+00  1.00000000e+00 -1.16328552e-16]
Error: 6.76039935100717e-33

Regularization: 0.1
Predictions: [0.17177929 0.82822071 0.82822071 0.17177929]
Error: 0.05897148782806046

Regularization: 1.0
Predictions: [0.44055584 0.55944416 0.55944416 0.44055584]
Error: 0.2460866515485878

Regularization: 10.0
Predictions: [0.5 0.5 0.5 0.5]
Error: 0.25
'''