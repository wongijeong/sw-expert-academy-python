T = int(input())

for i in range(T):
    N = int(input())
    ans = 0
    arr = list(map(int, input().split()))
    mx = 0

    for val in arr[::-1]:
        if val > mx:
            mx = val
        else:
            ans += mx - val
    print("#" + str(i + 1) + " " + str(ans))