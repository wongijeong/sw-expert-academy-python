T = int(input())
verification = [True] * T

for case in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    row_sum = 0
    col_sum = 0
    grid_sum = 0

    for i in range(9):
        for j in range(9):
            row_sum += sudoku[i][j]
            col_sum += sudoku[j][i]

        if row_sum != 45 or col_sum != 45:
            verification[case] = False
            row_sum = 0
            col_sum = 0
        else:
            row_sum = 0
            col_sum = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    grid_sum += sudoku[m][n]

            if grid_sum != 45:
                verification[case] = False
                grid_sum = 0
            else:
                grid_sum = 0

for case in range(T):
    if verification[case]:
        print(f"#{case + 1} {1}")
    else:
        print(f"#{case + 1} {0}")
