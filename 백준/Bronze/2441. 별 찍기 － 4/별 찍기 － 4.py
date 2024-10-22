import sys
N = int(sys.stdin.read().strip())
for i in range(1, N + 1):
    print(' ' * (i - 1) + '*' * (N - i + 1))