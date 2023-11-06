T = int(input())
currency = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
conut = [0] * 8

for case in range(T):
    N = int(input())

    for i in range(8):
        conut[i] = int(N / currency[i])
        N = N % currency[i]

    print(f"#{case + 1}")

    for i in range(8):
        print(conut[i], end=" ")

    print()