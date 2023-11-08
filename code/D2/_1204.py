from collections import Counter

T = int(input())

for case in range(T):
    case_num = int(input())
    student_score = list(map(int, input().split()))
    counting_score = Counter(student_score)

    # 리스트 컴프리헨션
    overlap_check = [k for k, v in counting_score.items() if max(counting_score.values()) == v]
    overlap_check.sort(reverse=True)

    print(f"#{case_num} {overlap_check[0]}")
