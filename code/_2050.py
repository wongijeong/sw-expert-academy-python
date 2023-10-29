alphabet = input()
alphabetList = list(alphabet)
alphabetAsciiList = []
lengthAlphabetList = len(alphabetList)

for i in range(lengthAlphabetList):
    alphabetAsciiList.append(ord(alphabetList[i]) - 64)

for i in range(lengthAlphabetList):
    print("%d " % int(alphabetAsciiList[i]), end="")
