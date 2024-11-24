promises = {
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
}
N = int(input())
is_changed = False

for _ in range(N):
    statement = input().strip()
    if statement not in promises:
        is_changed = True
        break
print("Yes" if is_changed else "No")