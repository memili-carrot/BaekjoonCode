def max_lan_length(K, N, lans):
    start, end = 1, max(lans)

    while start <= end:
        mid = (start + end) // 2
        total_cuts = sum(length // mid for length in lans)
        if total_cuts >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

print(max_lan_length(K, N, lans))