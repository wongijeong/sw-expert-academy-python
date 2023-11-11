for case in range(10):
    length = int(input())
    half_length = int(length / 2)
    char_array = [list(input()) for _ in range(8)]
    temp = ""
    count = 0

    if length % 2 == 0:
        for k in range(8):
            for i in range(9 - length):
                for j in range(i, i + length):
                    temp += char_array[k][j]
                if temp[0:half_length] == temp[length:half_length - 1:-1]:
                    count += 1
                temp = ""

        for k in range(8):
            for i in range(9 - length):
                for j in range(i, i + length):
                    temp += char_array[j][k]
                if temp[0:half_length] == temp[length:half_length - 1:-1]:
                    count += 1
                temp = ""

    elif length % 1 == 0:
        for k in range(8):
            for i in range(9 - length):
                for j in range(i, i + length):
                    temp += char_array[k][j]
                if temp[0:half_length] == temp[length + 1:half_length:-1]:
                    count += 1
                temp = ""

        for k in range(8):
            for i in range(9 - length):
                for j in range(i, i + length):
                    temp += char_array[j][k]
                if temp[0:half_length] == temp[length + 1:half_length:-1]:
                    count += 1
                temp = ""

    print(f"#{case + 1} {count}")
