n = int(input())
contains_7 = '7' in str(n)
divisible_7 = (n % 7 == 0)

if not contains_7 and not divisible_7:
    print(0)
elif not contains_7 and divisible_7:
    print(1)
elif contains_7 and not divisible_7:
    print(2)
else:
    print(3)