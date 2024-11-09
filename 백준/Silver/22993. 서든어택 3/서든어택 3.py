n = int(input())
array = list(map(int, input().split()))
attack = array[0]
others = sorted(array[1:])

p = True
for power in others:
    if attack > power:
        attack += power
    else:
        p = False
        break
print('Yes' if p else 'No')