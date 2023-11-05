T = int(input())

for case in range(T):
    N, K = map(int, (input().split()))  # N은 전체 학생 수, K는 조회 학생번호
    score = [list(map(int, input().split())) for _ in range(N)]
    ratio = int(N / 10)
    total_score = {}
    for i in range(1, N + 1):
        total_score[i] = score[i - 1][0] * 0.35 + score[i - 1][1] * 0.45 + score[i - 1][2] * 0.20

    total_score_sort = dict(sorted(total_score.items(), key=lambda x: x[1]))

    for i, (key, value) in enumerate(total_score_sort.items()):
        count = int(i / ratio)

        if count == 0:
            total_score_sort[key] = "D0"
        elif count == 1:
            total_score_sort[key] = "C-"
        elif count == 2:
            total_score_sort[key] = "C0"
        elif count == 3:
            total_score_sort[key] = "C+"
        elif count == 4:
            total_score_sort[key] = "B-"
        elif count == 5:
            total_score_sort[key] = "B0"
        elif count == 6:
            total_score_sort[key] = "B+"
        elif count == 7:
            total_score_sort[key] = "A-"
        elif count == 8:
            total_score_sort[key] = "A0"
        elif count == 9:
            total_score_sort[key] = "A+"

    print("#%d %s" % (case + 1, total_score_sort[K]))


