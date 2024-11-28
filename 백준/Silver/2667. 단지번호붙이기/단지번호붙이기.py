from collections import deque

def bfs(grid, visited, x, y, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    return count

def main():
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    complexes = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                count = bfs(grid, visited, i, j, n)
                complexes.append(count)
    complexes.sort()
    print(len(complexes))
    
    for count in complexes:
        print(count)

if __name__ == "__main__":
    main()