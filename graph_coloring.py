
def is_safe(graph, colors, vertex, color, n):
    for i in range(n):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True


def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n

    def solve(vertex):
        if vertex == n:
            return True

        for color in range(1, m + 1):
            if is_safe(graph, colors, vertex, color, n):
                colors[vertex] = color

                if solve(vertex + 1):
                    return True

                colors[vertex] = 0

        return False

    if solve(0):
        print("Valid coloring:", colors)
    else:
        print("Coloring solution does not exist")


# Test Case 1: Small complete graph
print("\nTest Case 1: Small Complete Graph")
graph1 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
graph_coloring(graph1, 3)


# Test Case 2: Triangle graph
print("\nTest Case 2: Triangle Graph")
graph2 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
graph_coloring(graph2, 3)


# Test Case 3: Bipartite graph
print("\nTest Case 3: Bipartite Graph")
graph3 = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
graph_coloring(graph3, 2)


# Test Case 4: One-vertex graph
print("\nTest Case 4: One-Vertex Graph")
graph4 = [[0]]
graph_coloring(graph4, 1)


# Test Case 5: Complete graph K4 with 3 colors
print("\nTest Case 5: Complete Graph K4 with 3 Colors")
graph5 = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]
graph_coloring(graph5, 3)