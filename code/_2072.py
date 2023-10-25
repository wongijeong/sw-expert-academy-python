T = int(input())

numberList = [[0 for col in range(10)] for row in range(T)]
result = [0] * T
i = 0

for i in range(T):
    numberList[i] = list(map(int, input().split()))

for i in range(T):
    for j in range(10):
        if (numberList[i][j] % 2) != 0:
            result[i] += numberList[i][j]

for i in range(T):
    print("#%d %d" % (i+1, result[i]))
