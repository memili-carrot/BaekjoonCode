N, M = map(int, input().strip().split())
baskets = [0] * N 

for _ in range(M):
    i, j, k = map(int, input().strip().split())
    for idx in range(i-1, j):
        baskets[idx] = k
        
print(" ".join(map(str, baskets))) #결과