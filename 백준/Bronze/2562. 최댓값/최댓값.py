inp = []

for i in range(9) :
    num = int(input())
    inp.append(num)

print(max(inp))
print(inp.index(max(inp)) + 1)