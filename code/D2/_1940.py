T = int(input())

for case in range(1, T + 1):
    N = int(input())  # Command의 개수, Time
    data = [list(map(int, input().split())) for _ in range(N)]  # data[i][0] 커맨드 종류 / data[i][1] 속도 절댓값
    RC_distance = 0
    RC_Speed = 0
    RC_acceleration = 0

    for time in range(N):
        if data[time][0] == 0:
            RC_Speed = RC_Speed
        elif data[time][0] == 1:
            RC_Speed += data[time][1]
        elif data[time][0] == 2:
            RC_Speed -= data[time][1]
            if RC_Speed < 0:
                RC_Speed = 0

        RC_distance += RC_Speed * 1

    print(f"#{case} {RC_distance}")

