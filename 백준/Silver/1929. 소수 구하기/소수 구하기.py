import sys
import math
input = sys.stdin.readline

def sieve_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    for k in range(m, n + 1):
        if is_prime[k]:
            print(k)

m, n = map(int, input().split())
sieve_eratosthenes(m, n)