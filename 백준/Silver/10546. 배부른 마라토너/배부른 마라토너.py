import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
participants = [input().strip() for _ in range(n)]
finishers = [input().strip() for _ in range(n - 1)]

participant_count = Counter(participants)
finisher_count = Counter(finishers)

for name in participant_count:
    if participant_count[name] != finisher_count[name]:
        print(name)
        break