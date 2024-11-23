N = list(map(int, input().split()))
if all(n in [0, 1] for n in N):
    print("S")
else:
    print("F")