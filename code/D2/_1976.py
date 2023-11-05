T = int(input())
hour = [0] * T
minute = [0] * T

for case in range(T):
    time = list(map(int, (input().split())))

    for i in range(4):
        if i == 0 or i == 2:
            hour[case] += time[i]
        else:
            minute[case] += time[i]

    if minute[case] >= 60:
        hour[case] += 1
        minute[case] -= 60

    if hour[case] >= 13:
        hour[case] -= 12

for case in range(T):
    print(f"#{case + 1} {hour[case]} {minute[case]}")
