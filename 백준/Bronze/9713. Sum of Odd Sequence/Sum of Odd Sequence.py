T = int(input())
results = []

for _ in range(T):
    N = int(input())
    results.append(((N + 1) // 2) ** 2)

for result in results:
    print(result)