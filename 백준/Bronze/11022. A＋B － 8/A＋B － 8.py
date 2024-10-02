T = int(input())
for e in range(T) :
    a , b = map(int, input().split())
    num = a+b
    print("Case #%d: %d + %d = %d" %(e+1,a,b,num))