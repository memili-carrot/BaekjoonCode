T = int(input())
for _ in range(T):
    stack = []
    is_vps = True
    for char in input():
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if stack:
        is_vps = False
    print("YES" if is_vps else "NO")