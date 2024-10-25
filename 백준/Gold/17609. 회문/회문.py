def pal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def near_pal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return check_pal(s, l + 1, r) or check_pal(s, l, r - 1)
        l += 1
        r -= 1
    return False

def check_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())

for _ in range(T):
    s = input()
    if pal(s):
        print(0)
    elif near_pal(s):
        print(1)
    else:
        print(2)