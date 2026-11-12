import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

n = int(input("Enter number of records: "))

data = []

for i in range(n):
    x = int(input("Enter X value: "))
    y = int(input("Enter Y value: "))
    data.append([x, y])

k = int(input("Enter number of clusters: "))

model = KMeans(n_clusters=k, random_state=0, n_init=10)
model.fit(data)

print("Cluster Labels:", model.labels_)
print("Cluster Centers:")
print(model.cluster_centers_)

# Plot the clusters
for i in range(k):
    cluster = [data[j] for j in range(n) if model.labels_[j] == i]
    plt.scatter(
        [p[0] for p in cluster],
        [p[1] for p in cluster],
        label="Cluster " + str(i)
    )

# Plot cluster centers
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("K-Means Clustering")
plt.legend()
plt.grid()
plt.show()
