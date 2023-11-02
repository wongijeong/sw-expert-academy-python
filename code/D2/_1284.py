T = int(input())
param = [[0 for col in range(5)] for row in range(T)]
costA, costB = [0] * T, [0] * T
"P, Q, R, S, W"

for i in range(T):
    param[i] = list(map(int, input().split()))

"A사: W * P 고정"
"B사: R <= W 경우 Q, R > W 경우 Q + W * S"
"A사와 B사와의 비교"

for i in range(T):
    costA[i] = param[i][4] * param[i][0]
    if param[i][4] <= param[i][2]:
        costB[i] = param[i][1]
    else:
        costB[i] = param[i][1] + (param[i][4] - param[i][2]) * param[i][3]

for i in range(T):
    if costA[i] < costB[i]:
        print("#%d %d" % (i + 1, costA[i]))
    else:
        print("#%d %d" % (i + 1, costB[i]))
