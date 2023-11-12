for test in range(10):
    case = int(input())
    char_array = [input() for _ in range(100)]
    max_palindrome_length = 0
    temp_string = ""

    # 가장 긴 가로 회문 구하기
    for i in range(100):
        for j in range(100):
            for k in range(j, 100):
                for m in range(j, k + 1):
                    temp_string += char_array[i][m]
                if len(temp_string) % 2 == 0:
                    if (temp_string[0:int(len(temp_string) / 2)] ==
                            temp_string[len(temp_string):int(len(temp_string) / 2) - 1:-1]):
                        if len(temp_string) > max_palindrome_length:
                            max_palindrome_length = len(temp_string)
                elif len(temp_string) % 1 == 0:
                    if (temp_string[0:int(len(temp_string) / 2)] ==
                            temp_string[len(temp_string) + 1:int(len(temp_string) / 2):-1]):
                        if len(temp_string) > max_palindrome_length:
                            max_palindrome_length = len(temp_string)
                temp_string = ""

    # 가장 긴 세로 회문 구하기
    for i in range(100):
        for j in range(100):
            for k in range(j, 100):
                for m in range(j, k + 1):
                    temp_string += char_array[m][i]
                if len(temp_string) % 2 == 0:
                    if (temp_string[0:int(len(temp_string) / 2)] ==
                            temp_string[len(temp_string):int(len(temp_string) / 2) - 1:-1]):
                        if len(temp_string) > max_palindrome_length:
                            max_palindrome_length = len(temp_string)
                elif len(temp_string) % 1 == 0:
                    if (temp_string[0:int(len(temp_string) / 2)] ==
                            temp_string[len(temp_string) + 1:int(len(temp_string) / 2):-1]):
                        if len(temp_string) > max_palindrome_length:
                            max_palindrome_length = len(temp_string)
                temp_string = ""

    print(f"#{case} {max_palindrome_length}")