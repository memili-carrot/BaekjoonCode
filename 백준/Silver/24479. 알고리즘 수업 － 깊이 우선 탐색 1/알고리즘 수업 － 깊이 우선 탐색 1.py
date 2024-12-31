import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline

def dfs(graph, visited, order, node):
    global count
    visited[node] = True
    order[node] = count
    count += 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, order, neighbor)

def main():
    n, m, r = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for key in graph:
        graph[key].sort()

    visited = [False] * (n + 1)
    order = [0] * (n + 1)
    global count
    count = 1

    dfs(graph, visited, order, r)

    for i in range(1, n + 1):
        print(order[i])

if __name__ == '__main__':
    main()