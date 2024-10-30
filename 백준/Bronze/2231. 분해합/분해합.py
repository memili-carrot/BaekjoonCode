def find_smallest(n):
    for m in range(max(1, n - 9 * len(str(n))), n):
        if m + sum(map(int, str(m))) == n:
            return m
    return 0

n = int(input())
print(find_smallest(n))