T = int(input())

for case in range(1, T + 1):
    a, b = map(int, input().split())
    result = a + b

    if result >= 24:
        result = result % 24

    print(f"#{case} {result}")
