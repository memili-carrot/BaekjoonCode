N = int(input().strip()) #입력
numbers = list(map(int, input().strip().split()))
v = int(input().strip())
count = numbers.count(v)
print(count) #출력