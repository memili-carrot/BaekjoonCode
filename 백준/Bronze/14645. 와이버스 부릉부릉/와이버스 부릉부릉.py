import sys
input = sys.stdin.readline

n, k = map(int, input().split())
passenger = k

for _ in range(n):
    a, b = map(int, input().split())
    passenger += a
    passenger -= b
print("비와이")