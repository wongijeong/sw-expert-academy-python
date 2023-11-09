for case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    temp = []
    view_value = 0
    for i in range(2, len(height) - 2):
        if (height[i - 2] < height[i] and height[i - 1] < height[i]
                and height[i + 1] < height[i] and height[i + 2] < height[i]):
            temp.append(height[i - 2])
            temp.append(height[i - 1])
            temp.append(height[i + 1])
            temp.append(height[i + 2])
            max_height = max(temp)
            temp.clear()
            view_value += height[i] - max_height

    print(f"#{case} {view_value}")

