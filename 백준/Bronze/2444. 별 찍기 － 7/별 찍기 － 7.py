N = int(input())
for i in range(1-N, N, 1):
    print(' '*abs(i)+'*'*abs(1-2*N+2*abs(i)))
