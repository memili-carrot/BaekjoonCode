import sys

for line in sys.stdin:
    if line.strip():
        n, s = map(int, line.split())
        print(s // (n + 1))