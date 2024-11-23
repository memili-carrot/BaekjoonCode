n = int(input())
password = [input().strip() for _ in range(n)]

for password in password:
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")