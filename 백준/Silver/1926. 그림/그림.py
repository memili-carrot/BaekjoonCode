from collections import deque
import sys

def bfs(grid, visited, x, y, n, m):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area += 1
    return area

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    num_pictures = 0
    max_area = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                num_pictures += 1
                max_area = max(max_area, bfs(grid, visited, i, j, n, m))
    print(num_pictures)
    print(max_area)

if __name__ == "__main__":
    main()