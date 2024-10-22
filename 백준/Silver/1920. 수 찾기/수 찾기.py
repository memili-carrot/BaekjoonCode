import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = set(map(int, data[1:N+1]))
M = int(data[N+1])
queries = map(int, data[N+2:N+2+M])

output = []
for query in queries:
    if query in A:
        output.append('1')
    else:
        output.append('0')
sys.stdout.write("\n".join(output) + "\n")