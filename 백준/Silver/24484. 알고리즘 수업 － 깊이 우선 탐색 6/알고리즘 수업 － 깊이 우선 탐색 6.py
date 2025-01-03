import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node, depth_value):
    global visit_order
    depth[node] = depth_value
    order[node] = visit_order
    visit_order += 1

    for nxt in graph[node]:
        if depth[nxt] == -1:
            dfs(nxt, depth_value + 1)

def main():
    n, m, r = map(int, input().split())

    global graph, depth, order, visit_order
    graph = [[] for _ in range(n + 1)]
    depth = [-1] * (n + 1)
    order = [0] * (n + 1)
    visit_order = 1

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
    dfs(r, 0)
    answer = 0
    for i in range(1, n + 1):
        answer += depth[i] * order[i]

    print(answer)

if __name__ == "__main__":
    main()