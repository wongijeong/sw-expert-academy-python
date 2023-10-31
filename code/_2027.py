shopPointer = 0

for i in range(5):
    for j in range(5):
        if shopPointer == j:
            print("#", end="")
        else:
            print("+", end="")
    shopPointer += 1
    print()
