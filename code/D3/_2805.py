T = int(input())

for case in range(1, T + 1):
    N = int(input())    # 농장의 크기 N x N
    half_index = int(N / 2)
    temp = list((input()) for _ in range(N))
    harvest = []
    harvest_sum = 0

    for i in range(N):
        harvest.append(list(temp[i]))

    for i in range(half_index + 1):
        for j in range(half_index, half_index + i + 1):
            harvest_sum += int(harvest[i][j])
        for j in range(half_index - 1, half_index - i - 1, -1):
            harvest_sum += int(harvest[i][j])

    for i, k in zip(range(N - 1, half_index, -1), range(half_index)):
        for j in range(half_index, half_index + k + 1):
            harvest_sum += int(harvest[i][j])
        for j in range(half_index - 1, half_index - k - 1, -1):
            harvest_sum += int(harvest[i][j])

    print(f"#{case} {harvest_sum}")
