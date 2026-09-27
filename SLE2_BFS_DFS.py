from collections import deque
import time

# Create a larger graph
graph = {}

for i in range(1, 101):
    graph[i] = []

# Connect nodes to form a tree-like graph
for i in range(1, 51):
    left = 2 * i
    right = 2 * i + 1

    if left <= 100:
        graph[i].append(left)

    if right <= 100:
        graph[i].append(right)


# BFS Algorithm
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_visited = 0

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            nodes_visited += 1

            if node == goal:
                return nodes_visited

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return nodes_visited


# DFS Algorithm
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_visited = 0

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            nodes_visited += 1

            if node == goal:
                return nodes_visited

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return nodes_visited


# Number of runs
runs = 1000

bfs_total_time = 0
dfs_total_time = 0

bfs_nodes = 0
dfs_nodes = 0


# BFS Testing
for i in range(runs):
    start_time = time.perf_counter()
    bfs_nodes = bfs(graph, 1, 100)
    end_time = time.perf_counter()

    bfs_total_time += (end_time - start_time)


# DFS Testing
for i in range(runs):
    start_time = time.perf_counter()
    dfs_nodes = dfs(graph, 1, 100)
    end_time = time.perf_counter()

    dfs_total_time += (end_time - start_time)


# Calculate average time
bfs_average = bfs_total_time / runs
dfs_average = dfs_total_time / runs


# Display results
print("BFS vs DFS Performance Analysis")
print("--------------------------------")
print("Number of Nodes in Graph: 100")
print("Start Node: 1")
print("Goal Node: 100")
print("Number of Runs:", runs)
print()

print("BFS:")
print("Nodes Visited:", bfs_nodes)
print("Average Execution Time:", bfs_average, "seconds")
print()

print("DFS:")
print("Nodes Visited:", dfs_nodes)
print("Average Execution Time:", dfs_average, "seconds")