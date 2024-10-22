from collections import deque
import sys
input = sys.stdin.read

def editor():
    data = input().splitlines()
    left_deque = deque(data[0])
    right_deque = deque()
    
    M = int(data[1])
    
    for i in range(2, M + 2):
        command = data[i]
        if command == 'L':
            if left_deque:
                right_deque.appendleft(left_deque.pop())
        elif command == 'D':
            if right_deque:
                left_deque.append(right_deque.popleft())
        elif command == 'B':
            if left_deque:
                left_deque.pop()
        elif command.startswith('P'):
            _, char = command.split()
            left_deque.append(char)
    print(''.join(left_deque + right_deque))
editor()