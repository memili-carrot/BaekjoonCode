n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    count = 1
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor)
    return count

infected_count = dfs(1) - 1
print(infected_count)