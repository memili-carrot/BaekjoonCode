from collections import deque
import sys
input = sys.stdin.read

def process_commands(commands):
    queue = deque()
    result = []
    for command in commands:
        if command.startswith("push"):
            _, num = command.split()
            queue.append(int(num))
        elif command == "pop":
            if queue:
                result.append(queue.popleft())
            else:
                result.append(-1)
        elif command == "size":
            result.append(len(queue))
        elif command == "empty":
            result.append(1 if not queue else 0)
        elif command == "front":
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        elif command == "back":
            if queue:
                result.append(queue[-1])
            else:
                result.append(-1)
    return result

commands = input().splitlines()
results = process_commands(commands[1:])

sys.stdout.write("\n".join(map(str, results)) + "\n")