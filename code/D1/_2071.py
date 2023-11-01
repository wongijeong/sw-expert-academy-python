T = int(input())
numberList = [[0 for col in range(10)]for row in range(T)]
temporarySpace = 0
averageResult = [0] * T

for i in range(T):
    numberList[i] = list(map(int, input().split()))

for i in range(T):
    for j in range(10):
        temporarySpace += numberList[i][j]
    averageResult[i] = round(temporarySpace / 10)
    temporarySpace = 0

for i in range(T):
    print("#%d %d" % (i + 1, averageResult[i]))
