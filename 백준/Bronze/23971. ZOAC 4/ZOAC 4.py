H, W, N, M = map(int, input().split())
rows = (H + N) // (N + 1)
cols = (W + M) // (M + 1)

max_participants = rows * cols
print(max_participants)