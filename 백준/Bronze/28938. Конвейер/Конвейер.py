n = int(input())
sequence = list(map(int, input().split()))
movement = sum(sequence)

if movement > 0:
    print("Right")
elif movement < 0:
    print("Left")
else:
    print("Stay")