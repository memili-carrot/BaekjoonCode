def temperature(n, m, temperature):
    current_sum = sum(temperature[:m])
    max_sum = current_sum

    for i in range(m, n):
        current_sum += temperature[i] - temperature[i - m]
        max_sum = max(max_sum, current_sum)
    return max_sum

n, m = map(int, input().split())
temperatures = list(map(int, input().split()))
print(temperature(n, m, temperatures))