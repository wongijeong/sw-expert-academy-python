T = int(input())

decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

for case in range(1, T + 1):
    word = input()
    bin_str = ''
    answer = ''

    for w in word:
        num = decode.index(w)
        bin_num = str(bin(num)[2:])     # 문자 하나 > 2진수 변환
        while len(bin_num) < 6:  # 0으로 앞자리부터 채워서 6비트로 만들기 zfill() 써도 됨
            bin_num = '0' + bin_num

        bin_str += bin_num  # 이진 6비트 차곡차곡 쌓기

    for i in range(len(bin_str) // 8):     # Word는 6비트로 변환하면서 6배 이를 8비트로 나누는 횟수
        ten_num = int(bin_str[i * 8:i * 8 + 8], 2)  # 8비트로 변환 후 10진수로 저장
        answer += chr(ten_num)  # 8비트로 저장된 10진수 하나하나를 문자열로 변환

    print(f"#{case} {answer}")
