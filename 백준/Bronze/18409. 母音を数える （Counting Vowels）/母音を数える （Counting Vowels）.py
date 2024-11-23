N = int(input())
S = input()
vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = sum(1 for char in S if char in vowels)
print(vowel_count)