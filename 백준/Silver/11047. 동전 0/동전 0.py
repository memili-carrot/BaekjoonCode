n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
count = 0

for coin in coins:
    if k == 0:
        break
    if coin <= k:
        count += k // coin
        k %= coin

print(count)