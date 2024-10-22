import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
numbers = list(map(int, data[1:]))

# 오름차순 정렬
numbers.sort()

for number in numbers:
    print(number)