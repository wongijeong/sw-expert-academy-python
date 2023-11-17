def queen(d, n, h):
    global count
    if d == n:
        count += 1
    else:
        for i in range(n):
            if i not in h:
                for x, y in enumerate(h):
                    if abs(d - x) == abs(i - y):
                        break
                else:
                    h.append(i)
                    queen(d + 1, n, h)
                    h.remove(i)


for case in range(int(input())):
    count = 0
    queen(0, int(input()), [])
    print(f"#{case + 1} {count}")
