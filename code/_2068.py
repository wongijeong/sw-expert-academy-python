T = int(input())

numberList = [[0 for col in range(10)] for row in range(T)]
maxResult = [0] * T
i = 0

for i in range(T):
    numberList[i] = list(map(int, input().split()))

for i in range(T):
    maxResult[i] = max(numberList[i])

for i in range(T):
    print("#%d %d" % (i+1, maxResult[i]))