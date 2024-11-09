import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
m = int(data[1])
graph = [[] for _ in range(n + 1)]
for line in data[2:2 + m]:
    a, b = map(int, line.split())
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