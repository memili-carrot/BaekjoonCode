import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node, d):
    depth[node] = d
    for nxt in graph[node]:
        if depth[nxt] == -1:
            dfs(nxt, d + 1)

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
    dfs(r, 0)

    for i in range(1, n + 1):
        print(depth[i])

if __name__ == "__main__":
    graph = []
    depth = []
    main()