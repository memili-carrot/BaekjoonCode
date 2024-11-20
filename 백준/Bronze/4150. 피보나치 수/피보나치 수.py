def fibonacci(n):
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b
    return b if n > 1 else a

n = int(input())
print(fibonacci(n))