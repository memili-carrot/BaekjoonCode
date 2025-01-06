import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    visit_order = 1
    visited[start] = True
    order[start] = visit_order
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                visit_order += 1
                order[v] = visit_order
                queue.append(v)

def main():
    n, m, r = map(int, input().split())

    global graph, visited, order
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    order = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        if graph[i]:
            graph[i].sort(reverse=True)
    bfs(r)

    print("\n".join(map(str, order[1:])))

if __name__ == "__main__":
    main()