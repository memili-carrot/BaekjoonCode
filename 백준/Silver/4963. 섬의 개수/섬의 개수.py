import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(x, y, w, h, map_data):
    map_data[y][x] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and map_data[ny][nx] == 1:
            dfs(nx, ny, w, h, map_data)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    map_data = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for y in range(h):
        for x in range(w):
            if map_data[y][x] == 1:
                dfs(x, y, w, h, map_data)
                count += 1
    print(count)