A, B = map(str, input().split(" "))
ex1 = ""
ex2 = ""

for i in range(len(A) - 1, -1, -1) :
    ex1 += A[i]

for i in range(len(B) - 1, -1, -1) :
    ex2 += B[i]

ex1 = int(ex1)
ex2 = int(ex2)

if ex1 > ex2 :
    print(ex1)
elif ex1 < ex2 :
    print(ex2)