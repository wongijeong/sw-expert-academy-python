T = int(input())

for case in range(1, T + 1):
    N = int(input())
    count = 0
    memo = set()
    correct = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    while memo != correct:
        count += 1
        dream = N * count
        temp = []
        for i in str(dream):
            temp.append(i)
        for i in temp:
            memo.add(int(i))

    print(f"#{case} {count * N}")
