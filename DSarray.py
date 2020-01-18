d = 4
a = [1, 2, 3, 4, 5]
arr = []

for x in range(len(a)):
    arr.append(a[(d + x) % len(a)])
print(' '.join(str(el) for el in arr))