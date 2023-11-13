# 거듭 제곱을 위한 함수
def involuition(x, y, n):
    if y == 1:
        return x
    return involuition(x * n, y - 1, n)


for test in range(10):
    case = int(input())
    M, N = map(int, input().split())

    print(f"#{case} {involuition(M, N, M)}")
