import sys

n = int(sys.stdin.readline().strip())
p = set()

for i in range(n):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        p.add(a)
    elif b == 'leave':
        p.discard(a)

print("\n".join(sorted(p, reverse=True)))