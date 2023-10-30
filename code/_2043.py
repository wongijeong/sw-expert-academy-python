checkCount = 0
P, K = map(int, input().split())

for i in range(K, 1000):
    checkCount += 1
    if i == P:
        break

print(checkCount)
