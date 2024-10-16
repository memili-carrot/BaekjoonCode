A, B = map(int, input().split())

# 작은 값과 큰 값을 구분
small = min(A, B)
large = max(A, B)

# 사이의 숫자 개수
if large - small - 1 > 0:
    print(large - small - 1)
    print(*range(small + 1, large))
else:
    print(0)