import sys
from collections import Counter
input = sys.stdin.readline

N = int(input().strip())

numbers = []
for _ in range(N):
    numbers.append(int(input().strip()))

mean = round(sum(numbers) / N)

numbers.sort()
median = numbers[N // 2]

# 최빈값 계산
counter = Counter(numbers)
most_common = counter.most_common()

# 빈도 높은 값들 추출
max_frequency = most_common[0][1]
frequent_numbers = []
for num, freq in most_common:
    if freq == max_frequency:
        frequent_numbers.append(num)

# 여러 개의 최빈값이 있을 때 두 번째로 작은 값 선택
frequent_numbers.sort()
if len(frequent_numbers) > 1:
    mode = frequent_numbers[1]
else:
    mode = frequent_numbers[0]

range_value = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_value)