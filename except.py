try:
    age = int(input("Insert number : "))
    income = 100
    risk = income / age
    print(age)
except ValueError:
    print("you need to enter an integer value")
except ZeroDivisionError:
    print("Number must be greater or less than 0")