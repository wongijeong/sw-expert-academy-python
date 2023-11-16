T = int(input())

for case in range(1, T + 1):

    num, count = input().split()
    count = int(count)
    array = [set([]) for _ in range(count + 1)]

    array[0].add(int(num))
    for j in range(1, count + 1):
        for x in array[j - 1]:
            temp = list(str(x))
            for k in range(0, len(temp) - 1):
                for m in range(k + 1, len(temp)):
                    temp2 = temp[:]
                    temp2[k], temp2[m] = temp2[m], temp2[k]
                    array[j].add(int(''.join(map(str, temp2))))

    print(f"#{case} {max(array[count])}")
