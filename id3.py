import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder


def run_id3(data, target, test):
data = data.copy().fillna("Missing")
test = test.copy().fillna("Missing")

X = data.drop(columns=[target])
y = data[target]

# Encode categorical input attributes
for col in X.columns:
if X[col].dtype == "object":
le = LabelEncoder()

# Include test categories to avoid unseen-label errors
values = list(X[col]) + list(test[col])
le.fit(values)

X[col] = le.transform(X[col])
test[col] = le.transform(test[col])

# Encode target class labels
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Create and train the ID3 decision tree
model = DecisionTreeClassifier(
criterion="entropy",
random_state=42
)
model.fit(X, y)

# Predict test cases
predictions = model.predict(test)
predictions = target_encoder.inverse_transform(predictions)

print("Prediction:", list(predictions))
print("Decision Tree:")
print(export_text(model, feature_names=list(X.columns)))
print("Depth:", model.get_depth())
print("Leaves:", model.get_n_leaves())


1. PLAY TENNIS DATASET
data1 = pd.DataFrame({
"Outlook": [
"Sunny", "Sunny", "Overcast", "Rain",
"Rain", "Rain", "Overcast", "Sunny",
"Sunny", "Rain", "Sunny", "Overcast",
"Overcast", "Rain"
 ],
"Temp": [
"Hot", "Hot", "Hot", "Mild",
"Cool", "Cool", "Cool", "Mild",
"Cool", "Mild", "Mild", "Mild",
"Hot", "Mild"
 ],
"Humidity": [
"High", "High", "High", "High",
"Normal", "Normal", "Normal", "High",
"Normal", "Normal", "Normal", "High",
"Normal", "High"
 ],
"Wind": [
"Weak", "Strong", "Weak", "Weak",
"Weak", "Strong", "Strong", "Weak",
"Weak", "Weak", "Strong", "Strong",
"Weak", "Strong"
 ],
"Play": [
"No", "No", "Yes", "Yes",
"Yes", "No", "Yes", "No",
"Yes", "Yes", "Yes", "Yes",
"Yes", "No"
 ]
})

test1 = pd.DataFrame({
"Outlook": ["Sunny"],
"Temp": ["Cool"],
"Humidity": ["High"],
"Wind": ["Strong"]
})

print("\n1. Play Tennis")
run_id3(data1, "Play", test1)


2. CLEAR CLASS SEPARATION
data2 = pd.DataFrame({
"Color": ["Red", "Red", "Red", "Blue", "Blue"],
"Size": ["Large", "Small", "Large", "Large", "Small"],
"Class": ["Apple", "Apple", "Berry", "Berry", "Berry"]
})

test2 = pd.DataFrame({
"Color": ["Blue"],
"Size": ["Small"]
})

print("\n2. Clear Class Separation")
run_id3(data2, "Class", test2)


3. MIXED ATTRIBUTES
data3 = pd.DataFrame({
"Age": [20, 25, 30, 35, 40, 45],
"Income": ["Low", "Low", "Medium", "Medium", "High", "High"],
"Student": ["Yes", "Yes", "No", "No", "No", "No"],
"Buy": ["Yes", "Yes", "No", "No", "No", "No"]
})

test3 = pd.DataFrame({
"Age": [28],
"Income": ["Medium"],
"Student": ["No"]
})

print("\n3. Mixed Attributes")
run_id3(data3, "Buy", test3)


4. ALL SAMPLES SAME CLASS
data4 = pd.DataFrame({
"Weather": ["Sunny", "Rain", "Cloudy", "Sunny"],
"Temp": ["Hot", "Cool", "Mild", "Hot"],
"Play": ["Yes", "Yes", "Yes", "Yes"]
})

test4 = pd.DataFrame({
"Weather": ["Rain"],
"Temp": ["Cool"]
})

print("\n4. All Samples Same Class")
run_id3(data4, "Play", test4)


5. MISSING ATTRIBUTE VALUES
data5 = pd.DataFrame({
"Outlook": ["Sunny", "Rain", None, "Sunny", "Rain"],
"Temp": ["Hot", None, "Mild", "Cool", "Cool"],
"Wind": ["Weak", "Strong", "Weak", None, "Strong"],
"Play": ["Yes", "No", "Yes", "Yes", "No"]
})

test5 = pd.DataFrame({
"Outlook": ["Sunny"],
"Temp": [None],
"Wind": ["Strong"]
})

print("\n5. Missing Attribute Values")
run_id3(data5, "Play", test5)