import sys
input = sys.stdin.readline

n = int(input().strip())
record = [input().strip() for _ in range(n)]

gomgom = 0
current_user = set()

for record in record:
    if record == "ENTER":
        current_user.clear()
    else:
        if record not in current_user:
            gomgom += 1
            current_user.add(record)
print(gomgom)