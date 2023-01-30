from collections import defaultdict

graph = defaultdict(list)
graph[1].append(2)
graph[2].append(3)
graph[4].append(1)

visited = set()

def dfs(node,graph,visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for v in graph[node]:
            dfs(v,graph,visited)
dfs(4, graph, visited)