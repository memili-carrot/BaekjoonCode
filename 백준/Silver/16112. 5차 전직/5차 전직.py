import sys

def max_arcane():
    n, k = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    ans = 0
    SUM = sum(lst[k:])
    for i in range(k - 1, -1, -1):
        ans += SUM
        SUM += lst[i]
    print(ans)

if __name__ == "__main__":
    max_arcane()