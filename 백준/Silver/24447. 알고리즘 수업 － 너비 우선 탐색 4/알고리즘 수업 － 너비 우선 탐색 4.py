import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    visit_order = 1
    depth[start] = 0
    order[start] = visit_order
    queue = deque([start])

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if depth[v] == -1:
                visit_order += 1
                depth[v] = depth[u] + 1
                order[v] = visit_order
                queue.append(v)

def main():
    n, m, r = map(int, input().split())

    global graph, depth, order
    graph = [[] for _ in range(n + 1)]
    depth = [-1] * (n + 1)
    order = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort()
    bfs(r)
    result = 0
    for i in range(1, n + 1):
        if depth[i] != -1:
            result += depth[i] * order[i]
    print(result)

if __name__ == "__main__":
    main()