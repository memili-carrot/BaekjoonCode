a, b, c = map(int, input().split())
sticks = sorted([a, b, c], reverse=True)
while sticks[0] >= sticks[1] + sticks[2]:
    sticks[0] -= 1
print(sum(sticks))