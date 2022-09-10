import copy

def verify(l: list):
    def expand_matrix():
        temp = copy.deepcopy(l)
        n = len(l[0])
        for row in temp:
            row.insert(0, 0)
            row.append(0)
        temp.insert(0, [0] * (n + 2))
        temp.append([0] * (n + 2))
        return temp

    def is_isolate(m: list, i: int, j: int):
        val = m[i - 1][j - 1] + m[i - 1][j] + m[i - 1][j + 1] + \
              m[i][j - 1] + m[i][j] + m[i][j + 1] + \
              m[i + 1][j - 1] + m[i + 1][j] + m[i + 1][j + 1]
        return val == 1

    m = expand_matrix()
    n = len(l[0])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # val = m[i][j]
            # boo = is_isolate(m, i, j)
            # if val and not boo:
            if m[i][j] == 1 and not is_isolate(m, i, j):
                return False
    return True


# matrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
matrix = [[0, 1, 0, 0, 1],
          [1, 0, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]
print(verify(matrix))
