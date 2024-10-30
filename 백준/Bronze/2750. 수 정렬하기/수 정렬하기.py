def sort_numbers(n):
    numbers = [int(input()) for _ in range(n)]
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print(number)

n = int(input())
sort_numbers(n)