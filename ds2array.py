import re

string = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""

arr1 = re.split('\n', string)
arr = []
for x in arr1:
    arr.append([int(s) for s in re.split("\s", x)])

def getLargestHourglass(): 
    largestHourglass = getHourglassSum(1, 1)
    for i in range(1,5):
        for j in range(1,5):
            if getHourglassSum(i, j) > largestHourglass: 
                largestHourglass = getHourglassSum(i, j)
            
    return largestHourglass


def getHourglassSum(x, y):
    return arr[x - 1][y - 1] + arr[x - 1][y] + arr[x - 1][y + 1] + arr[x][y] + arr[x + 1][y - 1] + arr[x + 1][y] + arr[x + 1][y + 1]

print(getLargestHourglass())