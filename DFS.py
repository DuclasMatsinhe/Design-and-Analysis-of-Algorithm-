def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("DFS Traversal:")
dfs(graph, 2)
