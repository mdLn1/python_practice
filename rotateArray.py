def rotate_array(arr, rotSize):
    if(rotSize >= len(arr)):
        rotSize %= arr
    return arr[rotSize:] + arr[:rotSize]

print(rotate_array("1 2 3 4 5".split(" "), 2))