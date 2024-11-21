def transform(s, t):
    while len(t) > len(s):
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1][::-1]
        else:
            break
    return 1 if t == s else 0

s = input().strip()
t = input().strip()

print(transform(s, t))