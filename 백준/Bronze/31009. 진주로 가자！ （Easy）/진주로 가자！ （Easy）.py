def bus_fare_check(n):
    fares = []
    jinju_fare = 0
    expensive_count = 0

    for _ in range(n):
        destination, cost = input().split()
        cost = int(cost)
        fares.append((destination, cost))
        if destination == "jinju":
            jinju_fare = cost
    for dest, fare in fares:
        if fare > jinju_fare:
            expensive_count += 1

    print(jinju_fare)
    print(expensive_count)

n = int(input())
bus_fare_check(n)