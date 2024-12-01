import sys

def sol(x):
    if visited[x]:
        return False
    visited[x] = 1
    for y in edge[x]:
        if not target[y] or sol(target[y]):
            target[y] = x
            return True
    return False

def main():
    input = sys.stdin.readline
    r, c, n = map(int, input().split())
    board = [[1] * c for _ in range(r)]
    for _ in range(n):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = 0
    ref = [[0] * c for _ in range(r)]
    ref2 = [[0] * c for _ in range(r)]
    row_num = 1
    for i in range(r):
        for j in range(c):
            ref[i][j] = row_num
        row_num += 1
    col_num = 1
    for j in range(c):
        for i in range(r):
            ref2[i][j] = col_num
        col_num += 1

    global edge
    edge = [[] for _ in range(row_num)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                edge[ref[i][j]].append(ref2[i][j])
    global target, visited
    target = [0] * col_num

    count = 0
    for i in range(1, row_num):
        visited = [0] * row_num
        if sol(i):
            count += 1
    print(count)

if __name__ == "__main__":
    main()