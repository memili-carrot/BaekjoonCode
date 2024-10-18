def find_last_computer(a, b):
    a %= 10
    if a == 0:
        return 10
    cycle = []
    value = a
    while value not in cycle:
        cycle.append(value)
        value = (value * a) % 10

    cycle_length = len(cycle)
    index = (b - 1) % cycle_length
    return cycle[index]
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(find_last_computer(a, b))