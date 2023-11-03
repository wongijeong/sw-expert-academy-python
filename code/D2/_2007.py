T = int(input())

for i in range(1, T + 1):
    string = input()
    word = ""
    for char in string:
        word += char
        if word * 2 in string:
            break

    print('#{} {}'.format(i, len(word)))
