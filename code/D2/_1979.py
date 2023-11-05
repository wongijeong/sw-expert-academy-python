T = int(input())

for case in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        puzzle[i].append(0)

    puzzle.append([0] * (N + 1))
    row_count = 0
    col_count = 0
    check = 0

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                row_count += 1
                if row_count == K and puzzle[i][j + 1] != 1:
                    check += 1
            else:
                row_count = 0

            if puzzle[j][i] == 1:
                col_count += 1
                if col_count == K and puzzle[j + 1][i] != 1:
                    check += 1
            else:
                col_count = 0

        row_count = 0
        col_count = 0

    print("#%d %d" % (case + 1, check))
