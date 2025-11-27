from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("BFS Traversal:")
bfs(graph, 2)
