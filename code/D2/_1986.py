T = int(input())
result = [0] * T

for case in range(T):
    N = int(input())
    temp = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            temp -= i
        else:
            temp += i
    result[case] = temp

for case in range(T):
    print(f"#{case + 1} {result[case]}")
