import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, OneClassSVM

iris = load_iris()
X, y = iris.data, iris.target


# --------------------------------------------------
# 1. Two class + Linear SVM
# --------------------------------------------------

# Select classes 0 and 1 and only first 2 features
X2 = X[y != 2, :2]
y2 = y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(
    X2, y2, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm = SVC(kernel="linear", C=1)
svm.fit(X_train, y_train)

print("Accuracy:", svm.score(X_test, y_test))
print("Support vectors:\n", svm.support_vectors_)


# --------------------------------------------------
# 2. Test point near margin
# --------------------------------------------------

d = svm.decision_function(X_test)
i = np.argmin(abs(d))

test = X_test[i]
prediction = svm.predict([test])

print("\nNear Margin point:", test)
print("Decision value:", d[i])
print("Prediction:", prediction[0])


# --------------------------------------------------
# 3. Plot SVM decision line
# --------------------------------------------------

w = svm.coef_[0]
b = svm.intercept_[0]

x = np.linspace(
    X_train[:, 0].min() - 1,
    X_train[:, 0].max() + 1,
    100
)

line = -(w[0] * x + b) / w[1]

# Margins
margin1 = -(w[0] * x + b - 1) / w[1]
margin2 = -(w[0] * x + b + 1) / w[1]

plt.figure(figsize=(8, 6))

# Data points
plt.scatter(
    X_train[:, 0],
    X_train[:, 1],
    c=y_train,
    cmap="coolwarm",
    label="Training Data"
)

# Decision line
plt.plot(
    x,
    line,
    "k-",
    label="Decision Boundary"
)

# Margins
plt.plot(
    x,
    margin1,
    "k--",
    label="Margin"
)

plt.plot(
    x,
    margin2,
    "k--"
)

# Support vectors
plt.scatter(
    svm.support_vectors_[:, 0],
    svm.support_vectors_[:, 1],
    s=150,
    facecolors="none",
    edgecolors="green",
    label="Support vectors"
)

# Test point
plt.scatter(
    test[0],
    test[1],
    marker="X",
    s=250,
    color="yellow",
    edgecolors="black",
    label="Test Point"
)

plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("Linear SVM - Iris Dataset")
plt.legend()
plt.grid()
plt.show()


# --------------------------------------------------
# 4. Overlapping Classes
# --------------------------------------------------

X3 = X[y != 0]
y3 = y[y != 0]

Xtr, Xte, ytr, yte = train_test_split(
    X3, y3, test_size=0.2, random_state=42
)

scaler2 = StandardScaler()
Xtr = scaler2.fit_transform(Xtr)
Xte = scaler2.transform(Xte)

svm2 = SVC(kernel="linear", C=1)
svm2.fit(Xtr, ytr)

print(
    "\nOverlapping classes accuracy:",
    svm2.score(Xte, yte)
)


# --------------------------------------------------
# 5. Single Class Training
# --------------------------------------------------

X_one = X[y == 0]

scaler3 = StandardScaler()
X_one = scaler3.fit_transform(X_one)

ocsvm = OneClassSVM(
    kernel="rbf",
    nu=0.05
)

ocsvm.fit(X_one)

X_all = scaler3.transform(X)
pred = ocsvm.predict(X_all)

print("\nOne Class SVM:")
print("+1 = Inlier, -1 = Outlier")
print(pred)