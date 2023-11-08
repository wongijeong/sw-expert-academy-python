d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
     '0110111': 8, '0001011': 9}
for i in range(int(input())):
    a = b = c = 0
    n, m = map(int, input().split())
    for _ in range(n):
        k = input()
        if '1' in k:
            r = k
    e = m - r[::-1].index('1')
    s = e - 56
    for j in range(8):
        c = d[r[s + j * 7:s + (j + 1) * 7]]
        if j % 2:
            a += c
            b += c
        else:
            a += 3 * c
            b += c
    print(f"#{i + 1}", b * (a % 10 == 0))
