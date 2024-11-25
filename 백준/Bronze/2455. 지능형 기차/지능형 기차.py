current_passenger = 0
max_passenger = 0

for _ in range(4):
    off, on = map(int, input().split())
    current_passenger = current_passenger - off + on
    max_passenger = max(max_passenger, current_passenger)
print(max_passenger)