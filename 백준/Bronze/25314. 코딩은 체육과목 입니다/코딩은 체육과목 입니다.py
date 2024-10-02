def generate_long_int_type(N):
    num_longs = N // 4
    return " ".join(["long"] * num_longs) + " int"
N = int(input().strip())
print(generate_long_int_type(N))