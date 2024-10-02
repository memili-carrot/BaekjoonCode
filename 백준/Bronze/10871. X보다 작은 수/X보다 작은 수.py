n, x = map(int, input().split(" "))
a = input()
a = a.split()
for i in a :
    if x > int(i) :
        print(int(i), end=" ")