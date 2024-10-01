n = int(input())
log = {}

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        log[name] = True
    elif status == "leave":
        if name in log:
            del log[name]

for name in sorted(log.keys(), reverse=True):
    print(name)