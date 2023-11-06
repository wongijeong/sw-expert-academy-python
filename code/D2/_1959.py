T = int(input())

for case in range(T):
    N, M = map(int, (input()).split())  # N은 A배열의 크기, M은 B 배열의 크기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    maxResult = 0

    if N > M:
        for i in range(N - M + 1):
            for k, j in zip(range(M), range(i, i + M)):
                result += B[k] * A[j]

            if maxResult < result:
                maxResult = result
                result = 0
            else:
                result = 0

    elif M > N:     # M = 5, N = 3, i = 0~2, j = 0~2, 1~3, 2~4
        for i in range(M - N + 1):
            for k, j in zip(range(N), range(i, i + N)):
                result += A[k] * B[j]

            if maxResult < result:
                maxResult = result
                result = 0
            else:
                result = 0

    else:
        for i in range(M):
            result += A[i] * B[i]

        if maxResult < result:
            maxResult = result

    print(f"#{case + 1} {maxResult}")
