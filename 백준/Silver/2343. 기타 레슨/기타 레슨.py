def count_bluerays(lessons, max_size):
    count = 1
    total = 0
    for lesson in lessons:
        if total + lesson > max_size:
            count += 1
            total = lesson
        else:
            total += lesson
    return count
def minimum_blueray_size(N, M, lessons):
    left = max(lesson for lesson in lessons)
    right = sum(lessons)
    
    while left <= right:
        mid = (left + right) // 2
        if count_bluerays(lessons, mid) <= M:
            right = mid - 1
        else:
            left = mid + 1
    return left

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

print(minimum_blueray_size(N, M, lessons))