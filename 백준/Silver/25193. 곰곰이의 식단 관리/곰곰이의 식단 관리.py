def chicken(S):
    N = len(S)
    chicken_count = S.count('C')
    other_count = N - chicken_count
    if chicken_count == 0:
        return 0
    if chicken_count == N:
        return N
    groups = other_count + 1
    base_size = chicken_count // groups
    extra = chicken_count % groups
    return base_size + (1 if extra > 0 else 0)

N = int(input())
S = input().strip()
print(chicken(S))