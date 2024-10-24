def max_hamster(n, m, holes):
    max_sum = 0
    current_sum = 0
    start = 0
    for end in range(n):
        current_sum += holes[end]
        while current_sum > m:
            current_sum -= holes[start]
            start += 1
        max_sum = max(max_sum, current_sum)

    return max_sum

n, m = map(int, input().split())
holes = list(map(int, input().split()))

print(max_hamster(n, m, holes))