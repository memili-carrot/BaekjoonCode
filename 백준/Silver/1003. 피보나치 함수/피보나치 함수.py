def fibonacci_count(t, test_cases):
    max_n = 40
    count_0, count_1 = [0] * (max_n + 1), [0] * (max_n + 1)
    count_0[0], count_1[0] = 1, 0
    count_0[1], count_1[1] = 0, 1

    for i in range(2, max_n + 1):
        count_0[i] = count_0[i - 1] + count_0[i - 2]
        count_1[i] = count_1[i - 1] + count_1[i - 2]

    results = []
    for n in test_cases:
        results.append((count_0[n], count_1[n]))
    return results

t = int(input())
test_cases = [int(input()) for _ in range(t)]
output = fibonacci_count(t, test_cases)

for res in output:
    print(res[0], res[1])