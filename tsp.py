# Travelling Salesman Problem
from itertools import permutations

def tsp(graph, start):
    n = len(graph)

    if n == 0:
        return 0, []

    if n == 1:
        return 0, [start]

    if start < 0 or start >= n:
        raise ValueError("Invalid start node")

    cities = [i for i in range(n) if i != start]

    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        cost = 0
        current = start

        for city in path:
            cost += graph[current][city]
            current = city

        cost += graph[current][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(path) + [start]

    return min_cost, best_path


# Example graph (cost matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start = 0
cost, path = tsp(graph, start)

print("Minimum tour cost:", cost)
print("Best path:", path)