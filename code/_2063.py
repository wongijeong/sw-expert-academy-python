N = int(input())

score = list(map(int, input().split()))

list.sort(score)

print("%d" % score[int(N/2)])
