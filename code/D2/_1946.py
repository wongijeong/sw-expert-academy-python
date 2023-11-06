T = int(input())

for case in range(1, T + 1):
    N = int(input())
    alphaList = [list(input().split()) for _ in range(N)]
    repetition = 0
    count = 0

    print(f"#{case}")

    for i in range(N):
        for j in range(int(alphaList[i][1])):
            print(alphaList[i][0], end="")
            count += 1
            if count % 10 == 0:
                print()

    print()
