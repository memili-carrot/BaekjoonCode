import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password_dict = {}
for _ in range(N):
    site, password = input().split()
    password_dict[site] = password
results = []
for _ in range(M):
    site = input().strip()
    results.append(password_dict[site])

print("\n".join(results))