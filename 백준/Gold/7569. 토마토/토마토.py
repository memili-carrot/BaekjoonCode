from collections import deque

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

queue = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((z, y, x))

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in directions:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

bfs()

max_day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:
                print(-1)
                exit()
            max_day = max(max_day, box[z][y][x])
print(max_day - 1)