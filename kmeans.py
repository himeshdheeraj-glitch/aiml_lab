import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

print("Upload the CSV file")
uploaded = files.upload()

filename = list(uploaded.keys())[0]
data = pd.read_csv(filename)

print("File uploaded successfully")
print(data.head())

X = data.select_dtypes(include=np.number).iloc[:, :3]

k = int(input("Enter number of clusters (k): "))

if k <= 0 or k > len(X):
    print("Invalid k")
else:
    centroids = X.to_numpy()[
        np.random.choice(len(X), k, replace=False)
    ]

    for _ in range(100):
        distances = np.sqrt(
            ((X.to_numpy()[:, None] - centroids) ** 2)
            .sum(axis=2)
        )

        labels = np.argmin(distances, axis=1)

        new_centroids = np.array([
            X.to_numpy()[labels == i].mean(axis=0)
            if np.any(labels == i)
            else centroids[i]
            for i in range(k)
        ])

        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    data["Cluster"] = labels + 1
    print(data)