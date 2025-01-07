import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    depth[start] = 0
    queue = deque([start])

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                queue.append(v)

def main():
    n, m, r = map(int, input().split())

    global graph, depth
    graph = [[] for _ in range(n + 1)]
    depth = [-1] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort()
    bfs(r)

    print("\n".join(map(str, depth[1:])))

if __name__ == "__main__":
    main()