N = int(input())
verification = [3, 6, 9]
digits = [0] * 3

"num = 33"
"(333%10) = 3"
"(333%100)/10 = 3"
"333/100= 3"

for num in range(1, N + 1):
    count = 0
    digits[0] = int(num / 100)
    digits[1] = int(num % 100 / 10)
    digits[2] = int(num % 10)

    for i in range(3):
        if digits[i] in verification:
            count += 1

    if count != 0:
        print("-" * count, end=" ")

    else:
        print(num, end=" ")
