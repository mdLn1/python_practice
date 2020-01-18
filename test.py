# string literals
first = 'john '
last = 'doe'
msg = f'{first} [{last}] is a legend'
print(msg)
print('john ' in msg)
# other string methods: upper, lower, find, replace, title
# arithmetic '//' integer division, '**' exponent
# round, abs
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment : ${down_payment}")

attempts = 0
max = 3
secret_number = 9
while attempts < max:
    guess = int(input(f"Guess {attempts+1} : "))
    attempts += 1
    if(guess == secret_number):
        print('You won')
        break
else:
    print("failed")
# range function creates an array