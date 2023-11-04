T = int(input())
string = []
count = 0

for case in range(T):
    string.append(input().strip())
    play = int(len(string[case]) / 2)

    for i in range(play):
        if string[case][i] == string[case][(len(string[case]) - 1) - i]:
            count = 1
        else:
            count = 0
            break

    print(f'#{case + 1} {count}')
