import sys
input = sys.stdin.read

def ironman_game(num, ws, ls, ts, names):
    score = 0
    for i in range(2 + p, 2 + p + num):
        name = data[i].strip()
        result = names.get(name)
        if result == 'W':
            score += ws
        else:
            score -= ls
            score = max(score, 0)
        if score >= ts:
            return 'I AM NOT IRONMAN!!'
    return 'I AM IRONMAN!!'

data = input().splitlines()
n, p = map(int, data[0].split())
ws, ls, ts = map(int, data[1].split())
names = {}
for i in range(2, 2 + p):
    k, v = data[i].split()
    names[k] = v

print(ironman_game(n, ws, ls, ts, names))