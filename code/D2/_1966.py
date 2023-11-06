T = int(input())

for case in range(T):
    N = int(input())
    numList = list(map(int, input().split()))
    numList.sort()

    print(f"#{case + 1}", end= " ")

    for i in range(N):
        print(f"{numList[i]}", end=" ")

    print()

