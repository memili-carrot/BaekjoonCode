def atm_min_wait(n, times):
    times.sort()
    total = wait = 0
    for t in times:
        wait += t
        total += wait
    return total

n = int(input())
times = list(map(int, input().split()))

print(atm_min_wait(n, times))