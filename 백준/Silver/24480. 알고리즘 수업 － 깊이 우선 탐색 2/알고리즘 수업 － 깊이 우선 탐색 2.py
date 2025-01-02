import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global visit_order
    visited[node] = True
    order[node] = visit_order
    visit_order += 1

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

def main():
    n, m, r = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
    dfs(r)

    for i in range(1, n + 1):
        print(order[i])

graph = defaultdict(list)
visited = []
order = []
visit_order = 1

if __name__ == "__main__":
    input_data = input().split()
    n, m, r = map(int, input_data)

    visited = [False] * (n + 1)
    order = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
    dfs(r)

    for i in range(1, n + 1):
        print(order[i])