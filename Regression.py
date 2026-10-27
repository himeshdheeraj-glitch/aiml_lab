import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Upload CSV file
files.upload()

d = pd.read_csv("Salary-Data.csv")

print(d.head(), "\nRows:", len(d))

X = d[["YearsExperience"]].values
y = d["Salary"].values

# TEST 1: Best-fit line
m = LinearRegression().fit(X, y)
s = m.coef_[0]
c = m.intercept_

print("\nTEST 1")
print("Equation: Salary =", s, "* Experience +", c)
print("PASS" if s != 0 else "FAIL")

# TEST 2: Train-test
Xt, Xv, yt, yv = train_test_split(
    X, y, test_size=1/3, random_state=0
)

m2 = LinearRegression().fit(Xt, yt)
yp = m2.predict(Xv)

mse = mean_squared_error(yv, yp)
r2 = r2_score(yv, yp)

print("\nTEST 2")
print("Actual:", yv)
print("Predicted:", np.round(yp, 2))
print("MSE:", mse, "R2:", r2)
print("PASS" if r2 > 0.5 else "FAIL")

# TEST 3: Positive correlation
print("\nTEST 3")
print("Positive slope:", s)
print("PASS" if s > 0 else "FAIL")

# TEST 4: Constant target
yc = np.full(len(y), np.mean(y))
mc = LinearRegression().fit(X, yc)

print("\nTEST 4")
print("Slope:", mc.coef_[0])
print("PASS" if abs(mc.coef_[0]) < 1e-6 else "FAIL")

# TEST 5: Outlier
yo = y.copy()
yo[np.argmax(yo)] *= 5

mo = LinearRegression().fit(X, yo)

normal_mse = mean_squared_error(y, m.predict(X))
outlier_mse = mean_squared_error(yo, mo.predict(X))

print("\nTEST 5")
print("Normal MSE:", normal_mse)
print("Outlier MSE:", outlier_mse)
print("PASS" if outlier_mse > normal_mse else "FAIL")

# GRAPHS

# Training data
plt.scatter(Xt, yt)
plt.plot(Xt, m2.predict(Xt))
plt.title("Training Data")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Testing data
plt.scatter(Xv, yv)
plt.plot(Xv, yp)
plt.title("Testing Data")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()