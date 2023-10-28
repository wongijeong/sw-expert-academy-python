N = int(input())

result = 0
digits = [0] * 4
divingNumber = 1000

for i in range(4):
    digits[i] = int(N / divingNumber)
    N %= divingNumber
    divingNumber /= 10

for i in range(4):
    result += digits[i]

print("%d" % result)
