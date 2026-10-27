def a_star_algo(start_node, stop_node, graph_node, h_dict):
open_set = {start_node}
closed_set = set()

g = {start_node: 0}
parents = {start_node: start_node}

while open_set:
n = min(
open_set,
key=lambda v: g[v] + h_dict.get(v, 0)
)

if n == stop_node:
path = []

while parents[n] != n:
path.append(n)
n = parents[n]

path.append(start_node)
path.reverse()

cost = g[stop_node]
print("Path found:", path)
print("Total cost:", cost)
return path, cost

open_set.remove(n)
closed_set.add(n)

for m, weight in graph_node.get(n, {}).items():
tentative_g = g[n] + weight

if tentative_g < g.get(m, float("inf")):
g[m] = tentative_g
parents[m] = n

if m in closed_set:
closed_set.remove(m)

open_set.add(m)

print("Path not found")
return None, float("inf")


Test Case 1: Graph with admissible heuristic
print("\nTest Case 1: Admissible Heuristic")
graph1 = {
'S': {'A': 1, 'B': 4},
'A': {'G': 5},
'B': {'G': 1},
'G': {}
}
h1 = {'S': 0, 'A': 5, 'B': 1, 'G': 0}
a_star_algo('S', 'G', graph1, h1)


Test Case 2: Multiple possible paths
print("\nTest Case 2: Multiple Paths")
graph2 = {
'S': {'A': 2, 'B': 1},
'A': {'G': 2},
'B': {'G': 5},
'G': {}
}
h2 = {'S': 0, 'A': 0, 'B': 0, 'G': 0}
a_star_algo('S', 'G', graph2, h2)


Test Case 3: Direct start-goal connection
print("\nTest Case 3: Direct Connection")
graph3 = {
'S': {'G': 2, 'A': 1},
'A': {'G': 5},
'G': {}
}
h3 = {'S': 0, 'A': 5, 'G': 0}
a_star_algo('S', 'G', graph3, h3)


Test Case 4: Goal not reachable
print("\nTest Case 4: Goal Not Reachable")
graph4 = {
'S': {'A': 1},
'A': {},
'B': {'G': 1},
'G': {}
}
h4 = {'S': 0, 'A': 1, 'B': 1, 'G': 0}
a_star_algo('S', 'G', graph4, h4)


Test Case 5: Misleading heuristic
print("\nTest Case 5: Misleading Heuristic")
graph5 = {
'S': {'A': 2, 'B': 1},
'A': {'G': 2},
'B': {'G': 1},
'G': {}
}
h5 = {'S': 0, 'A': 0, 'B': 100, 'G': 0}
a_star_algo('S', 'G', graph5, h5)