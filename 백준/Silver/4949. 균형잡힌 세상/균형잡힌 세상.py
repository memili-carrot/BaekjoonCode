import sys
input = sys.stdin.read

def is_balanced(string):
    stack = []
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

lines = input().splitlines()

for line in lines:
    if line == ".":
        break
    print(is_balanced(line))