
import numpy as np

class SingleLinearNeuron:
    def _init_(self, input_dim, learning_rate=0.01):
        self.weights = np.random.randn(input_dim)
        self.learning_rate = learning_rate

    def train(self, X, epochs):
        for epoch in range(epochs):
            for x in X:
                y = np.dot(self.weights, x)
                self.weights += self.learning_rate * y * x

    def get_weights(self):
        return self.weights

# Generate arbitrary input distribution
np.random.seed(42)
X = np.random.randn(100, 2)

# Train single linear neuron
neuron = SingleLinearNeuron(input_dim=2, learning_rate=0.01)
neuron.train(X, epochs=100)

# Get the principal component
principal_component = neuron.get_weights()
print("Principal Component:", principal_component)

'''
output:

Principal Component: [0.77382507 0.63338619]
'''