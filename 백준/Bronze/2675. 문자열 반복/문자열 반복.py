T = int(input())
ex = []

if T >= 1 and T <= 1000 :
    for cnt in range(T) :
        inp = input().split()
        R = int(inp[0])
        S = inp[1]
        P = ""

        for i in S :
            ex.append(i)
        
        if R >= 1 and R <= 8 :
            if len(S) >= 1 and len(S) <= 20 :
                for j in S :
                    P += j * R

        print(P)