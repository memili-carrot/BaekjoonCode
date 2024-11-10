import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

symmetric_diff = A.symmetric_difference(B)
print(len(symmetric_diff))