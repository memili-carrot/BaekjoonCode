from collections import deque

def find_fastest_time(n, k):
    visited = [False] * 100001
    queue = deque([(n, 0)])
    visited[n] = True

    while queue:
        current, time = queue.popleft()
        if current == k:
            return time
        for next_position in (current - 1, current + 1, current * 2):
            if 0 <= next_position <= 100000 and not visited[next_position]:
                visited[next_position] = True
                queue.append((next_position, time + 1))

n, k = map(int, input().split())
print(find_fastest_time(n, k))