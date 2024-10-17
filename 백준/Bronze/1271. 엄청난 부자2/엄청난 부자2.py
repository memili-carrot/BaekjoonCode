def money(n, m):
    quotient = n // m
    remainder = n % m
    
    print(quotient)
    print(remainder)

n, m = map(int, input().split())

money(n, m)