def count_zeros(n):
    zeros = 0
    while n > 1:
        zeros += n // 5
        n //= 5
    return zeros

n = int(input())
print(count_zeros(n))