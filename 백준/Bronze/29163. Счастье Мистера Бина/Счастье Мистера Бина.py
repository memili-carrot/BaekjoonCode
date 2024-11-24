n = int(input())
number = list(map(int, input().split()))
even_number = sum(1 for number in number if number % 2 == 0)
odd_number = n - even_number

if even_number > odd_number:
    print("Happy")
else:
    print("Sad")