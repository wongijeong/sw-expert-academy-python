for test in range(10):
    case = int(input())
    number_array = [list(map(int, input().split())) for _ in range(100)]
    row_sum = 0
    col_sum = 0
    diagonal_sum_1 = 0
    diagonal_sum_2 = 0
    max_sum = 0

    for i in range(100):
        for j in range(100):
            row_sum += number_array[i][j]

        if max_sum < row_sum:
            max_sum = row_sum
        row_sum = 0

    for i in range(100):
        for j in range(100):
            col_sum += number_array[j][i]

        if max_sum < col_sum:
            max_sum = col_sum
        col_sum = 0

    for i in range(100):
        diagonal_sum_1 += number_array[i][i]

        if max_sum < diagonal_sum_1:
            max_sum = diagonal_sum_1
        diagonal_sum_1 = 0

    for i, j in zip(range(100), range(99, -1, -1)):
        diagonal_sum_2 += number_array[i][j]

        if max_sum < diagonal_sum_2:
            max_sum = diagonal_sum_2
        diagonal_sum_2 = 0

    print(f"#{case} {max_sum}")

