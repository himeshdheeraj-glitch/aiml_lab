from collections import deque

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Depth-First Search (DFS)
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# Function to run both algorithms
def run_test(test_name, graph, start):
    print("\n" + "=" * 50)
    print(test_name)
    print("=" * 50)

    print("BFS Traversal:", end=" ")
    bfs(graph, start)

    print("\nDFS Traversal:", end=" ")
    visited = set()
    dfs(graph, start, visited)
    print("\n")


# Test Case 1: Connected graph starting with node A
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
run_test("Test Case 1: Connected Graph Starting at A", graph1, 'A')


# Test Case 2: Graph with multiple branches
graph2 = {
    0: [1, 2, 3],
    1: [4, 5],
    2: [6, 7],
    3: [8, 9],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
run_test("Test Case 2: Graph with Multiple Branches", graph2, 0)


# Test Case 3: Cyclic graph
graph3 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
run_test("Test Case 3: Cyclic Graph", graph3, 0)


# Test Case 4: Single-node graph
graph4 = {
    'A': []
}
run_test("Test Case 4: Single-Node Graph", graph4, 'A')


# Test Case 5: Disconnected graph
graph5 = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}
run_test("Test Case 5: Disconnected Graph (Starting at 0)", graph5, 0)