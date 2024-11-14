def count_paper(x, y, size):
    global white_count, blue_count
    initial_color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != initial_color:
                half_size = size // 2
                count_paper(x, y, half_size)
                count_paper(x, y + half_size, half_size)
                count_paper(x + half_size, y, half_size)
                count_paper(x + half_size, y + half_size, half_size)
                return
    if initial_color == 0:
        white_count += 1
    else:
        blue_count += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_count = 0
blue_count = 0
count_paper(0, 0, n)

print(white_count)
print(blue_count)