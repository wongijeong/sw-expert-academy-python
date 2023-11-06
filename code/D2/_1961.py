T = int(input())

for case in range(T):
    N = int(input())
    numList = [list(map(int, input().split())) for _ in range(N)]
    ang_90 = [] * (N * 3)
    ang_180 = [] * (N * 3)
    ang_270 = [] * (N * 3)

    print(f"#{case + 1}")

    # 90도
    for i in range(N):
        for j in range(N - 1, -1, -1):
            ang_90.append(numList[j][i])

    # 180도
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            ang_180.append(numList[i][j])

    # 270도
    for i in range(N - 1, -1, -1):
        for j in range(N):
            ang_270.append(numList[j][i])

    for i in range(0, N * N, N):
        for j in range(i, i + N):
            print(ang_90[j], end="")
        print(end=" ")
        for j in range(i, i + N):
            print(ang_180[j], end="")
        print(end=" ")
        for j in range(i, i + N):
            print(ang_270[j], end="")
        print()

