T = int(input())
numList = []

for case in range(T):
    numList.append(list(map(int, input().split())))
    numList[case].sort()

for case in range(T):
    print("#%d %d" % (case + 1, (round(sum(numList[case][1:9]) / 8))))
