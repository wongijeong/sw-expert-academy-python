T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for a in range(N - M + 1):
        for b in range(N - M + 1):
            value = 0
            for row in range(a, a + M):
                for col in range(b, b + M):
                    value += arr[row][col]

            if max_value < value:
                max_value = value

    print("#%d %d" % (i + 1, max_value))
