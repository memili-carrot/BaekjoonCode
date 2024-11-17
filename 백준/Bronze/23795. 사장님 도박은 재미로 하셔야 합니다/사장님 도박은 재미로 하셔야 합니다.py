import sys

total = 0

while True:
    betting = int(sys.stdin.readline().strip())
    if betting == -1:
        break
    total += betting

print(total)