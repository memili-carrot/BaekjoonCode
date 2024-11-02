def Rev(num):
    return int(str(num)[::-1])

X, Y = map(int, input().split())
result = Rev(Rev(X) + Rev(Y))
print(result)