from collections import deque

n = int(input())
parrots = [deque(input().split()) for _ in range(n)]
cseteram = input().split()

for word in cseteram:
    found = False
    for parrot in parrots:
        if parrot and parrot[0] == word:
            parrot.popleft()
            found = True
            break
    if not found:
        print("Impossible")
        exit()

for parrot in parrots:
    if parrot:
        print("Impossible")
        exit()
print("Possible")