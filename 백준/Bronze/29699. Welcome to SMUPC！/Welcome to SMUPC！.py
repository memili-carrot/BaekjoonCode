label = "WelcomeToSMUPC"
N = int(input())
result = label[(N - 1) % len(label)]
print(result)