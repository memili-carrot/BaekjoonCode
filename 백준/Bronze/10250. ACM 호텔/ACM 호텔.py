import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if floor == 0:
        floor = H
    
    room = (N // H) + 1
    if N % H == 0:
        room = N // H
    print(f"{floor}{room:02d}")