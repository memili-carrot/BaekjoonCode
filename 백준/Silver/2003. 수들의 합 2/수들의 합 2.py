def count_sum(n, m, arr):
    start, end = 0, 0
    sum = 0
    count = 0

    while end < n:
        sum += arr[end]

        while sum >= m:
            if sum == m:
                count += 1
            sum -= arr[start]
            start += 1
        end += 1
    return count

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(count_sum(n, m, arr))