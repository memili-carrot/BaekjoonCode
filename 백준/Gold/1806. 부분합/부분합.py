def min_len(target, nums):
    n = len(nums)
    start, end = 0, 0
    min_len = float('inf')
    curr_sum = 0

    while True:
        if curr_sum >= target:
            min_len = min(min_len, end - start)
            curr_sum -= nums[start]
            start += 1
        elif end == n:
            break
        else:
            curr_sum += nums[end]
            end += 1
    return 0 if min_len == float('inf') else min_len

n, target = map(int, input().split())
nums = list(map(int, input().split()))

result = min_len(target, nums)
print(result)