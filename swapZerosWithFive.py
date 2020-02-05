def convertFive(n):
    numStr = list(str(n))
    for index, el in enumerate(numStr):
        if(el == "0"):
            numStr[index] = "5"
    return int("".join(numStr))

print(convertFive(32031))