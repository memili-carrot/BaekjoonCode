alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
a = []
result = []

alp = str(input())

if len(alp) < 101 :
    for i in alp :
        a.append(i)

    for i in alphabet :
        if a.count(i) == 0 :
            result.append(-1)
        else :
            result.append(a.index(i))

    for i in result :
        print(i, end = " ")