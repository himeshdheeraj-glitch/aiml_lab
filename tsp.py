
from itertools import permutations

def tsp(graph, start):
    n = len(graph)
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

    print("Minimum Cost:", min_cost)
    print("Best Path:", best_path)


# Test Case 1: 4 Cities
print("\nTest Case 1: 4 Cities")
graph1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tsp(graph1, 0)


# Test Case 2: 3 Cities
print("\nTest Case 2: 3 Cities")
graph2 = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]
tsp(graph2, 0)


# Test Case 3: 4 Cities with Different Costs
print("\nTest Case 3: Different Costs")
graph3 = [
    [0, 5, 10, 15],
    [5, 0, 9, 10],
    [10, 9, 0, 8],
    [15, 10, 8, 0]
]
tsp(graph3, 0)


# Test Case 4: 2 Cities
print("\nTest Case 4: 2 Cities")
graph4 = [
    [0, 10],
    [10, 0]
]
tsp(graph4, 0)


# Test Case 5: 5 Cities
print("\nTest Case 5: 5 Cities")
graph5 = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]
tsp(graph5, 0)
