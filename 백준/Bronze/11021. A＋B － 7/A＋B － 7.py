t = int(input())
for i in range(t):
    i += 1
    a, b = map(int, input().split())
    print("Case #%s: %s" %(i, a + b))