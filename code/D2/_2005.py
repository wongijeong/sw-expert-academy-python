T = int(input())

for i in range(T):
    N = int(input())
    value = [0] * N
    temp = [0] * N
    print("#%d" % (i + 1))
    for j in range(N):
        for m in range(N):
            temp[m] = value[m]
        for k in range(j + 1):
            if k != 0 and k != j:
                value[k] = temp[k - 1] + temp[k]
            else:
                value[k] = 1
        for m in range(j + 1):
            print(value[m], end=" ")
        print()

    "value[1, 1, 1, 1 > temp[1, 1, 1, 1] 저장"
    "value[1, 2, 1, 1] > value[1] = temp[0] + temp[1], temp[1, 2, 1, 1]에 저장"
    "value[1, 3, 3, 1] > value[1] = temp[0] + temp[1], value[2] = temp[1] + temp[2]"
