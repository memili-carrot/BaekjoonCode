import sys
input = sys.stdin.readline
N, M = map(int, input().split())

unheard_set = set()
for _ in range(N):
    unheard_set.add(input().strip())
unseen_set = set()
for _ in range(M):
    unseen_set.add(input().strip())
result_set = unheard_set & unseen_set
result_list = sorted(result_set)
print(len(result_list))
for name in result_list:
    print(name)