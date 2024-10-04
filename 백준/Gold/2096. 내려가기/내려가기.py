N = int(input())
max_dp = min_dp = list(map(int, input().split()))

for _ in range(1, N):
    a, b, c = map(int, input().split())
    max_dp = [
        max(max_dp[0], max_dp[1]) + a,
        max(max_dp[0], max_dp[1], max_dp[2]) + b,
        max(max_dp[1], max_dp[2]) + c
    ]    
    min_dp = [
        min(min_dp[0], min_dp[1]) + a,
        min(min_dp[0], min_dp[1], min_dp[2]) + b,
        min(min_dp[1], min_dp[2]) + c
    ]
print(max(max_dp), min(min_dp))