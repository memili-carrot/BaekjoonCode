num = []

for i in range(10) :
    n = int(input())
    n = n % 42
    num.append(n)

num = set(num)

print(len(num))