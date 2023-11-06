T = int(input())
month_day = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
             '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

for case in range(1, T + 1):
    dateData = list(map(int, input().split()))
    dayGap = 0

    for i in range(dateData[0], dateData[2]):
        if i == dateData[0]:
            dayGap += month_day[str(i)] - dateData[1] + 1
        else:
            dayGap += month_day[str(i)]

    dayGap += dateData[3]

    print(f"#{case} {dayGap}")
