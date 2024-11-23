MOD = 20000303

N = input().strip()
remainder = 0
for digit in N:
    remainder = (remainder * 10 + int(digit)) % MOD
print(remainder)