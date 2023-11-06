T = int(input())

for case in range(T):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 방향 벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0

    x = 0
    y = -1
    num = 1
    while num <= (N * N):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            snail[nx][ny] = num
            x, y = nx, ny
            num += 1
        else:
            i = (i + 1) % 4

    print(f"#{case + 1}")

    for i in snail:
        print(*i)
