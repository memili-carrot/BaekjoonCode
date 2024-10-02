from collections import deque

def find_password(logs):
    left_stack = deque()
    right_stack = deque()
    
    for char in logs:
        if char == '-':
            if left_stack:
                left_stack.pop()
        elif char == '<':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.popleft())
        else:
            left_stack.append(char)
    
    return ''.join(left_stack) + ''.join(right_stack)

t = int(input())

for _ in range(t):
    logs = input()
    result = find_password(logs)
    print(result)