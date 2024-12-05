import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def bfs():
    queue = deque()
    for employee in range(1, n + 1):
        if aMatch[employee] == 0:
            level[employee] = 0
            queue.append(employee)
        else:
            level[employee] = INF
    level[0] = INF

    while queue:
        current = queue.popleft()
        if level[current] < level[0]:
            for task in adj[current]:
                if level[bMatch[task]] == INF:
                    level[bMatch[task]] = level[current] + 1
                    queue.append(bMatch[task])
    return level[0] != INF

def dfs(employee):
    if employee:
        for task in adj[employee]:
            if level[bMatch[task]] == level[employee] + 1 and dfs(bMatch[task]):
                aMatch[employee] = task
                bMatch[task] = employee
                return True
        level[employee] = INF
        return False
    return True

def solution():
    match_count = 0
    while bfs():
        for employee in range(1, n + 1):
            if aMatch[employee] == 0:
                match_count += dfs(employee)
    print(match_count)

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for employee in range(1, n + 1):
        data = list(map(int, input().split()))
        adj[employee].extend(data[1:])
    aMatch = [0] * (n + 1)
    bMatch = [0] * (m + 1)
    level = [INF] * (n + 1)

    solution()