N, K = map(int, input().split())
count = 0
sieve = [True] * (N + 1)

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if sieve[j]:
            sieve[j] = False
            count += 1
            if count == K:
                print(j)
                exit()