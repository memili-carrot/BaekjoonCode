def pyramid_blocks():
    while True:
        base = int(input())
        if base == 0:
            break
        print(sum(range(1, base + 1)))
pyramid_blocks()