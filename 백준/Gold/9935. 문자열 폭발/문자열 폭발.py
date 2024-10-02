def explode_string(s, bomb):
    stack = []
    bomb_length = len(bomb)
    
    for char in s:
        stack.append(char)
        if ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]
    
    if not stack:
        return "FRULA"
    else:
        return ''.join(stack)

s = input()
bomb = input()

print(explode_string(s, bomb))