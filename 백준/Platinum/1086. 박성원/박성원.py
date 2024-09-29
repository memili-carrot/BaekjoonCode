import math
N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())
mods = []
lens_mod = []
for num in nums:
    mod_val = int(num) % K
    mods.append(mod_val)
    lens_mod.append(pow(10, len(num), K))
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1
for mask in range(1 << N):
    for mod in range(K):
        if dp[mask][mod] == 0:
            continue
        for i in range(N):
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                new_mod = (mod * lens_mod[i] + mods[i]) % K
                dp[new_mask][new_mod] += dp[mask][mod]
p = dp[(1 << N) - 1][0]
q = math.factorial(N)
if p == 0:
    print("0/1")
else:
    g = math.gcd(p, q)
    print(f"{p // g}/{q // g}")