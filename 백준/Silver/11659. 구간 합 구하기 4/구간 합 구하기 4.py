import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

results = []
for _ in range(m):
    i, j = map(int, input().split())
    results.append(prefix_sum[j] - prefix_sum[i - 1])

print("\n".join(map(str, results)))