numbers = [0,1,2,3,4,5,1]
numbers.append(6)
numbers.insert(0,7)
numbers.pop()
numbers.index(3)
numbers.count(1)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
numbers.clear()

# for checking if element exists in an array better to use 'el in array' because arr.index returns ValueError if not found

numbers3 = [1,1,2,3,4,4,5]
uniques = []

for number in numbers3:
    if(number in uniques):
        continue
    uniques.append(number)

# print(uniques)

# tuples make sure that elements cannot be changed in an array like object
tuple1 = (1,2,5)
# decomposing into variables need to make sure that the number of els is equal to the num of vars
x,y,z = tuple1

print(x)