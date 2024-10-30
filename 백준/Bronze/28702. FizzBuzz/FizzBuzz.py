def next_fizzbuzz(prev_three):
    for i in range(3, 0, -1):
        x = prev_three[3 - i]
        if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
            n = int(x) + i
            break
    return 'Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or str(n)

prev_three = [input().strip() for _ in range(3)]
print(next_fizzbuzz(prev_three))