def build_zero_matrix(row: int, col: int):
    matrix = []
    for r in range(row):
        matrix.append([])
        for c in range(col):
            matrix[r].append(0)
    return (matrix)


def set_bomb(matrix: list, row_col: list) -> list:
    row = row_col[0] - 1
    col = row_col[1] - 1
    main_row = len(matrix)
    main_col = len(matrix[0])
    matrix[row][col] = "*"
    # updatein the matrix

    directions = [(-1, 1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]

    for r, c in directions:
        curr_r = row + r
        curr_c = col + c

        if matrix[curr_r, curr_c] != "*" and 0 <= curr_r < main_row and 0 <= curr_c < main_col:
            matrix[curr_r, curr_c] += 1

    return (matrix)


if __name__ == '__main__':
    row, col = map(int, input().split())
    bomb_num = int(input())

    bombs = []
    for b in range(bomb_num):
        bomb = list(map(int, input().split()))
        bombs.append(bomb)

    matrix = build_zero_matrix(row, col)
    for bomb in bombs:
        matrix = set_bomb(matrix, bomb)

    for row in matrix:
        row = list(map(str, row))
        print(" ".join(row))
