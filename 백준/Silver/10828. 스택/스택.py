import sys
input = sys.stdin.read
commands = input().splitlines()
stack = []

for command in commands[1:]:
    if command.startswith("push"):
        _, value = command.split()
        stack.append(int(value))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if not stack else 0)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)