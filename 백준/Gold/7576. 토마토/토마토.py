from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
bfs()

max_day = 0
for row in box:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        max_day = max(max_day, value)
print(max_day - 1)