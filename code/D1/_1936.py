A, B = map(int, input().split())
strA, strB = "", ""

if A == 1:
    strA = "가위"
elif A == 2:
    strA = "바위"
elif A == 3:
    strA = "보"

if B == 1:
    strB = "가위"
elif B == 2:
    strB = "바위"
elif B == 3:
    strB = "보"

if strA == "가위":
    if strB == "바위":
        print("B")
    elif strB == "보":
        print("A")
elif strA == "바위":
    if strB == "가위":
        print("A")
    elif strB == "보":
        print("B")
elif strA == "보":
    if strB == "가위":
        print("B")
    elif strB == "바위":
        print("A")
