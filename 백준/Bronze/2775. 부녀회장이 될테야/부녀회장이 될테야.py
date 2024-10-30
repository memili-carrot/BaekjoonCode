def num_people(k, n):
    apt = [[i for i in range(n + 1)] for _ in range(k + 1)]
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            apt[floor][room] = apt[floor][room - 1] + apt[floor - 1][room]
    return apt[k][n]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(num_people(k, n))