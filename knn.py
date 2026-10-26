
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Main KNN program
print("K-NEAREST NEIGHBOR CLASSIFICATION")

file_name = input("Enter CSV file path (press Enter for sample data): ")

if file_name.strip():
    df = pd.read_csv(file_name)
else:
    # Sample dataset if no CSV file is provided
    df = pd.DataFrame({
        "Height": [150, 155, 160, 165, 170, 175, 180, 185],
        "Weight": [45, 50, 55, 60, 65, 70, 75, 80],
        "Class": ["A", "A", "A", "A", "B", "B", "B", "B"]
    })

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("Actual Labels:", list(y_test))
print("Predicted Labels:", list(y_pred))


# Test Case 1: Labeled dataset, k = 3
print("\nTest Case 1: Labeled Dataset")

X1 = [[1], [2], [3], [8], [9], [10]]
y1 = ["A", "A", "A", "B", "B", "B"]

model1 = KNeighborsClassifier(n_neighbors=3)
model1.fit(X1, y1)
print("Prediction for 2.5:", model1.predict([[2.5]])[0])


# Test Case 2: Numeric feature dataset
print("\nTest Case 2: Numeric Feature Dataset")

X2 = [[1, 2], [2, 3], [3, 3], [8, 8], [9, 8], [10, 9]]
y2 = ["A", "A", "A", "B", "B", "B"]

model2 = KNeighborsClassifier(n_neighbors=3)
model2.fit(X2, y2)
print("Prediction for [2, 2]:", model2.predict([[2, 2]])[0])


# Test Case 3: Clearly separated classes
print("\nTest Case 3: Clearly Separated Classes")

X3 = [[1], [2], [3], [10], [11], [12]]
y3 = ["A", "A", "A", "B", "B", "B"]

model3 = KNeighborsClassifier(n_neighbors=3)
model3.fit(X3, y3)
print("Prediction for 11:", model3.predict([[11]])[0])


# Test Case 4: Tie among neighbors
print("\nTest Case 4: Tie Among Neighbors")

X4 = [[0], [2]]
y4 = ["A", "B"]

model4 = KNeighborsClassifier(n_neighbors=2)
model4.fit(X4, y4)
print("Prediction for 1:", model4.predict([[1]])[0])
print("Note: Both classes have equal votes.")


# Test Case 5: k larger than dataset
print("\nTest Case 5: k Larger Than Dataset")

X5 = [[1], [2], [3]]
y5 = ["A", "A", "B"]

k = 5

if k > len(X5):
    print("Error: k is larger than the dataset.")
else:
    model5 = KNeighborsClassifier(n_neighbors=k)
    model5.fit(X5, y5)
    print("Prediction:", model5.predict([[2]])[0])