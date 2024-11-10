import sys
import heapq

input = sys.stdin.readline
min_heap = []

n = int(input().strip())
for _ in range(n):
    x = int(input().strip())
    if x > 0:
        heapq.heappush(min_heap, x)
    elif x == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)