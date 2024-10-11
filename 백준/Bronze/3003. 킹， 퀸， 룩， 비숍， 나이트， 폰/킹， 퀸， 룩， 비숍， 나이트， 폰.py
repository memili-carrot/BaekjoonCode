default_pieces = [1, 1, 2, 2, 2, 8]
found_pieces = list(map(int, input().split()))
result = [default_pieces[i] - found_pieces[i] for i in range(6)]
print(" ".join(map(str, result)))
