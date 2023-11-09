for case in range(1, 11):
    dump_count = int(input())
    box_height = list(map(int, input().split()))

    for i in range(dump_count):
        if max(box_height) != min(box_height):
            box_height[box_height.index(max(box_height))] -= 1
            box_height[box_height.index(min(box_height))] += 1

    result = max(box_height) - min(box_height)

    print(f"#{case} {result}")
