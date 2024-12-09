import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y, color, grid, visited, n):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
            dfs(nx, ny, color, grid, visited, n)

def count_regions(grid, n, is_colorblind):
    visited = [[False] * n for _ in range(n)]
    regions = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                regions += 1
                if is_colorblind and grid[i][j] in "RG":
                    dfs(i, j, "R", grid, visited, n)  # R과 G를 동일하게 처리
                else:
                    dfs(i, j, grid[i][j], grid, visited, n)
    return regions

def main():
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    normal_regions = count_regions(grid, n, False)
    colorblind_grid = [["R" if c == "G" else c for c in row] for row in grid]
    colorblind_regions = count_regions(colorblind_grid, n, True)
    print(normal_regions, colorblind_regions)

if __name__ == "__main__":
    main()