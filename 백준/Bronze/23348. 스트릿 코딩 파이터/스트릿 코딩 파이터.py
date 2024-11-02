import sys
input = sys.stdin.readline

level = list(map(int, input().split()))
n = int(input())
max_score = 0

for _ in range(n):
    team_score = 0
    for _ in range(3):
        a = list(map(int, input().split()))
        team_score += sum(a[i] * level[i] for i in range(3))
    max_score = max(max_score, team_score)
print(max_score)