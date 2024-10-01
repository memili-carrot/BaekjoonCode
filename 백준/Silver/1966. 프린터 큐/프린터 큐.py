from collections import deque

def printer_queue(test_cases):
    for case in test_cases:
        N, M = case[0]
        priorities = case[1]
        queue = deque([(i, p) for i, p in enumerate(priorities)])
        count = 0
        
        while queue:
            current = queue.popleft()
            if any(current[1] < q[1] for q in queue):
                queue.append(current)
            else:
                count += 1
                if current[0] == M:
                    print(count)
                    break

test_cases = []
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    test_cases.append(((N, M), priorities))

printer_queue(test_cases)