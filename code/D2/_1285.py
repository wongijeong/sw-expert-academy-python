T = int(input())

for case in range(1, T + 1):
    N = int(input())
    stone_position = list(map(int, input().split()))
    min_position = abs(stone_position[0])
    people_count = 0
    for i in range(N):
        if min_position > abs(stone_position[i]):
            min_position = abs(stone_position[i])

    for i in range(N):
        if min_position == abs(stone_position[i]):
            people_count += 1

    print(f"#{case} {min_position} {people_count}")
