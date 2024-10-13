s = input().upper()
c = list(set(s))
p = []

for i in c:
    p.append(s.count(i))
    
if p.count(max(p)) > 1:
    print("?")
else:
    print(c[p.index(max(p))])