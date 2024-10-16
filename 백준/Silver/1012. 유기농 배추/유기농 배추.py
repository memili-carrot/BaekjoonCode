import sys
sys.setrecursionlimit(10000)

# 상, 하, 좌, 우 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# DFS로 배추밭을 탐색하며 연결된 배추를 모두 방문 처리
def dfs(x, y, field, visited, N, M):
    visited[y][x] = True  # 현재 위치 방문 처리
    # 상하좌우로 이동하면서 인접한 배추를 찾음
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and field[ny][nx] == 1:
            dfs(nx, ny, field, visited, N, M)

# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로, N: 세로, K: 배추 위치 개수
    field = [[0] * M for _ in range(N)]  # 배추밭을 0으로 초기화
    visited = [[False] * M for _ in range(N)]  # 방문 여부 체크

    # 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1  # 배추가 심어져 있으면 1로 표시

    # 필요한 배추흰지렁이 수 (그룹 수)
    worm_count = 0

    # 모든 배추밭을 탐색
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:  # 배추가 있고, 아직 방문하지 않았다면
                dfs(x, y, field, visited, N, M)  # 새로운 그룹 탐색 시작
                worm_count += 1  # 새로운 그룹이 발견될 때마다 카운트

    # 결과 출력
    print(worm_count)