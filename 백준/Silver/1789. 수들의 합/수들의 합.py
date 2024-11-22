S = int(input())
sum = 0
N = 0

while sum + (N + 1) <= S:
    N += 1
    sum += N
print(N)