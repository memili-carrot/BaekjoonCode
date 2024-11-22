def dfs(n, idx, expression):
    if idx > n:
        if eval(expression.replace(' ', '')) == 0:
            print(expression)
        return
    next_num = str(idx)
    dfs(n, idx + 1, expression + ' ' + next_num)
    dfs(n, idx + 1, expression + '+' + next_num)
    dfs(n, idx + 1, expression + '-' + next_num)

t = int(input())
for _ in range(t):
    n = int(input())
    dfs(n, 2, '1')
    print()