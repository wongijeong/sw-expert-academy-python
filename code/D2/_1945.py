T = int(input())
count = [[0 for col in range(5)] for row in range(T)]

for case in range(T):
    num = int(input())

    while num % 2 == 0:
        num /= 2
        count[case][0] += 1

    while num % 3 == 0:
        num /= 3
        count[case][1] += 1

    while num % 5 == 0:
        num /= 5
        count[case][2] += 1

    while num % 7 == 0:
        num /= 7
        count[case][3] += 1

    while num % 11 == 0:
        num /= 11
        count[case][4] += 1

for case in range(T):
    print(f"#{case + 1}", end=" ")
    for i in range(5):
        print("%d" % count[case][i], end=" ")
    print()