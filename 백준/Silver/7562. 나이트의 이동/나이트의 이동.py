from collections import deque


def bfs(l, start, end):
    directions = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]

    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == end:
            return moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))
    return -1


def main():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    results = []

    for _ in range(t):
        l = int(input().strip())
        start = tuple(map(int, input().strip().split()))
        end = tuple(map(int, input().strip().split()))
        results.append(bfs(l, start, end))
    for result in results:
        print(result)


if __name__ == "__main__":
    main()