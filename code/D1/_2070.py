def comparison(a, b):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="


T = int(input())

numberList = [[0 for col in range(2)] for row in range(T)]

for i in range(T):
    numberList[i] = list(map(int, input().split()))

for i in range(T):
    for j in range(1):
        print("#%d %s" % (i + 1, comparison(numberList[i][j], numberList[i][j + 1])))
