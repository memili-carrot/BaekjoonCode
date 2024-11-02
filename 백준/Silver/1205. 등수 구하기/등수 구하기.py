n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank_list = list(map(int, input().split()))

    if n == p and rank_list[-1] >= score:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if rank_list[i] <= score:
                result = i + 1
                break
        print(result)