def handling(mm, day):
    if mm == "01" or mm == "03" or mm == "05" or mm == "07" or mm == "08" or mm == "10" or mm == "12":
        if day[0] != "0" and day[0] != "1" and day[0] != "2" and day[0] != "3":
            return True
        elif day[0] == "0":
            if day[1] == "0":
                return True
            else:
                return False
        elif day[0] == "1":
            return False
        elif day[0] == "2":
            return False
        elif day[0] == "3":
            if day[1] == "0":
                return False
            elif day[1] == "1":
                return False
            else:
                return True

    elif mm == "04" or mm == "06" or mm == "09" or mm == "11":
        if day[0] != "0" and day[0] != "1" and day[0] != "2" and day[0] != "3":
            return True
        elif day[0] == "0":
            if day[1] == "0":
                return True
            else:
                return False
        elif day[0] == "1":
            return False
        elif day[0] == "2":
            return False
        elif day[0] == "3":
            if day[1] == "0":
                return False
            else:
                return True

    elif mm == "02":
        if day[0] != "0" and day[0] != "1" and day[0] != "2":
            return True
        elif day[0] == "0":
            if day[1] == "0":
                return True
            else:
                return False
        elif day[0] == "1":
            return False
        elif day[0] == "2":
            if day[1] == "9":
                return True
        else:
            return True

    else:
        return True


T = int(input())

dateArr = [""] * T

for i in range(T):
    dateArr[i] = input()
    dateArr[i] = dateArr[i][0:4] + "/" + dateArr[i][4:6] + "/" + dateArr[i][6:]

for i in range(T):
    temp = dateArr[i].split("/")
    if handling(temp[1], temp[2]):
        dateArr[i] = "-1"
    print("#%d %s" % ((i+1), dateArr[i]))
