import sys
from collections import deque
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())
grid = [list(map(int, line.split())) for line in data[1:]]
distance = [[-1 if grid[i][j] == 1 else 0 for j in range(m)] for i in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start = (i, j)
            distance[i][j] = 0
            break
    if start:
        break
        
queue = deque([start])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
while queue:
    x, y = queue.popleft()
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

for row in distance:
    print(" ".join(map(str, row)))