N = int(input())

for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * i
    print(spaces + stars)

for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i)
    stars = '*' * i
    print(spaces + stars)