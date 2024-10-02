A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B + C

hours = (total_minutes // 60) % 24
minutes = total_minutes % 60

print(hours, minutes)