T = int(input())
share = [] * T
rest = [] * T

for i in range(T):
    a, b = map(int, input().split())
    share.append(int(a / b))
    rest.append(a % b)

for i in range(T):
    print("#%d %d %d" % (i+1, share[i], rest[i]))
