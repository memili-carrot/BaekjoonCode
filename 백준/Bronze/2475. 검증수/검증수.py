numbers = list(map(int, input().split()))
sum_of_squares = sum([num**2 for num in numbers])
verification_number = sum_of_squares % 10
print(verification_number)