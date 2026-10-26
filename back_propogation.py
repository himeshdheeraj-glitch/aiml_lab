import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
def show(title, x, y, hidden=3, lr=0.1, epochs=1000):
    print(f"\n{'='*55}\n{title}\n{'='*55}")
    m = MLPRegressor(
        hidden_layer_sizes=(hidden,),
        learning_rate_init=lr,
        max_iter=epochs,
        random_state=42
    )
    m.fit(x, y)
    p = m.predict(x)
    print("Input:\n", x)
    print("Actual:", y)
    print("Predicted:", np.round(p, 2))
    return m, p
# TEST-1: NON-LINEAR XOR
x1 = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y1 = np.array([0, 100, 100, 0])
show("Test-1: Non-Linear dataset", x1, y1)
print("Reason: XOR is non-linear and requires a hidden layer")
# COMMON DATASET FOR TEST 2-5
x = np.array([[2, 9], [1, 5], [3, 6]])
y = np.array([92, 86, 89])
# TEST-2: SMALL NEURAL NETWORK
show("Test-2: Small neural network", x, y, hidden=1)
print("Reason: One hidden neuron gives limited learning capacity")
# TEST-3: TRAINING ERROR
m, p = show("Test-3: Reduction in Training Error", x, y)
loss = m.loss_curve_
print("\nTraining loss")
for e in [1, 10, 50, 100, 500, 1000, 5000, len(loss)]:
    if e <= len(loss):
        print(f"Epoch {e}: {loss[e-1]:.6f}")
print("\nFinal prediction:", np.round(p, 2))
print("Final MSE:", round(mean_squared_error(y, p), 6))
plt.plot(range(1, len(loss) + 1), loss)
plt.xlabel("Epochs")
plt.ylabel("Training Loss")
plt.title("Reduction in Training Error")
plt.grid()
plt.show()
print("Reason: More epochs allow more weight updates through back propagation")
# TEST-4: VERY HIGH LEARNING RATE
m, p = show(
    "Test-4: Very high learning rate",
    x,
    y,
    lr=10,
    epochs=100
)
print("Learning rate: 10")
print("Reason: A very high learning rate can make training unstable")
# TEST-5: ZERO EPOCH
print(f"\n{'='*55}\nTest-5: Zero Epoch\n{'='*55}")
print("Input:\n", x)
print("Actual:", y)
print("Epochs: 0")
print("Reason: max_iter=0 cannot train an MLPRegressor")
print("Therefore, this case is demonstrated conceptually")
print(f"\n{'='*55}\nAll Test Cases Completed\n{'='*55}")