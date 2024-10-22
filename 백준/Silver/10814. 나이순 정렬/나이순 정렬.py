import sys
input = sys.stdin.read

def sort_members():
    data = input().splitlines()
    
    N = int(data[0])
    members = []
    
    for i in range(1, N + 1):
        age, name = data[i].split()
        members.append((int(age), name))
    members.sort(key=lambda x: x[0])
    for member in members:
        print(member[0], member[1])

sort_members()