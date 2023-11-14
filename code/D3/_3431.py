T = int(input())

for case in range(1, T + 1):
    L, U, X = map(int, input().split())

    if L > X:
        result = L - X

    else:
        if U < X:
            result = -1
        else:
            result = 0

    print(f"#{case} {result}")
