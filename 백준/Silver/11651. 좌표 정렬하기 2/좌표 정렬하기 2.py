import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
cor = [list(map(int, line.split())) for line in data[1:]]
cor.sort(key=lambda x: (x[1], x[0]))

for x, y in cor:
    print(f"{x} {y}")