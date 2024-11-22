def find_primes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(m, n + 1) if is_prime[i]]
    if primes:
        return sum(primes), min(primes)
    else:
        return -1, -1

m = int(input())
n = int(input())

prime_sum, prime_min = find_primes(m, n)
if prime_sum == -1:
    print(-1)
else:
    print(prime_sum)
    print(prime_min)