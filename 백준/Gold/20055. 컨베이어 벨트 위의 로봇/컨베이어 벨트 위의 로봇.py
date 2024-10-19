from collections import deque

def process(n, k, a):
    belt = deque(a)
    robots = deque([False] * n)
    zero = 0
    count = 0

    while True:
        count += 1
        belt.rotate(1)
        robots.rotate(1)
        robots[-1] = False
        for i in range(n-2, -1, -1):
            if robots[i] and not robots[i+1] and belt[i+1] > 0:
                robots[i] = False
                robots[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    zero += 1

        robots[-1] = False

        if belt[0] > 0:
            robots[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                zero += 1
        if zero >= k:
            break

    return count

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = process(n, k, a)
print(result)