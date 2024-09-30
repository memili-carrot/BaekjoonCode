from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]
start_x, start_y = 0, 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start_x, start_y = i, j
            break
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    people_count = 0
    while queue:
        x, y = queue.popleft()
        if campus[x][y] == 'P':
            people_count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if campus[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return people_count
result = bfs(start_x, start_y)
if result == 0:
    print("TT")
else:
    print(result)