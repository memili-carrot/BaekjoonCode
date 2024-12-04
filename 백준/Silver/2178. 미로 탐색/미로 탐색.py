from collections import deque

def maze_solver():
    import sys
    input = sys.stdin.read
    data = input().split()

    N, M = map(int, data[0:2])
    maze = [list(map(int, list(data[i + 2]))) for i in range(N)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    print(maze[N-1][M-1])

if __name__ == "__main__":
    maze_solver()