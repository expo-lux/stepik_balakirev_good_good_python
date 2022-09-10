N = int(input())
identity_matrix = [[1 if row == col else 0 for col in range(N)]
                   for row in range(N)]
for row in identity_matrix:
    print(*row)
