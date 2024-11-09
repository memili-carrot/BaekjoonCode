import sys
input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m):
    arr = input().split()
    command = arr[0]
    if command == 'add':
        s.add(int(arr[1]))
    elif command == 'remove':
        s.discard(int(arr[1]))
    elif command == 'check':
        if int(arr[1]) in s:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        x = int(arr[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif command == 'all':
        s = set(range(1, 21))
    elif command == 'empty':
        s.clear()