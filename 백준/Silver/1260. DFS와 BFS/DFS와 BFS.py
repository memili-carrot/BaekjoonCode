from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    dfs_result.append(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    queue = deque([start])
    visited = [False] * (len(graph))
    visited[start] = True
    bfs_result = []

    while queue:
        node = queue.popleft()
        bfs_result.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return bfs_result

if __name__ == "__main__":
    # 입력 받기
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, w = map(int, input().split())
        graph[u].append(w)
        graph[w].append(u)

    for i in range(1, n + 1):
        graph[i].sort()

    visited = [False] * (n + 1)
    dfs_result = []
    dfs(graph, v, visited)

    bfs_result = bfs(graph, v)

    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))