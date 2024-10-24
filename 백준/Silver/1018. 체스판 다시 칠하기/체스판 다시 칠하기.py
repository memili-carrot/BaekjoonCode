#주어진 8x8 크기의 구역에서 첫 번째 칸이 흰색('W') 또는 검은색('B')일 때
#체스판처럼 칠하기 위해 몇 개의 칸을 다시 칠해야 하는지를 계산

def count_paint(board, start_row, start_col, first_color):
    paint_count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                expected_color = first_color
            else:
                expected_color = 'B' if first_color == 'W' else 'W'
            
            if board[start_row + i][start_col + j] != expected_color:
                paint_count += 1
    return paint_count

def min_paint_chessboard(board, N, M):
    min_paint = float('inf')
    
    for i in range(N - 7):
        for j in range(M - 7):
            paint_w = count_paint(board, i, j, 'W')
            paint_b = count_paint(board, i, j, 'B')
            min_paint = min(min_paint, paint_w, paint_b)
    
    return min_paint

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

print(min_paint_chessboard(board, N, M))