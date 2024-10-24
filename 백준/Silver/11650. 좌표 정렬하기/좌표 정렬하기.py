import sys
N = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
points.sort(key=lambda point: (point[0], point[1]))

for point in points:
    print(point[0], point[1])