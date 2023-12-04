lines_with_calibration_values = []
with open('input.txt', encoding="utf-8") as f:
    lines_with_calibration_values = f.readlines()
f.closed

digits = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

digits_in_words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

digits_starting_letters = {
    'o': 3,
    't': 5,
    'f': 4,
    's': 5,
    'e': 5,
    'n': 4
}

calibration_values = []

def get_calibration_value(input):
    first_and_last_digits = [0, 0]
    i = 0
    for i in range(len(input)):
        x = input[i]
        if x in digits:
            if first_and_last_digits[0] == 0:
                first_and_last_digits[0] = int(x)
            first_and_last_digits[1] = int(x)
            

        starting_letter = digits_starting_letters.get(x, 0)

        if starting_letter != 0:
            for x in digits_in_words.keys():
                if input.startswith(x, i, i + starting_letter):
                    if first_and_last_digits[0] == 0:
                        first_and_last_digits[0] = digits_in_words[x]
                    first_and_last_digits[1] = digits_in_words[x]

    return first_and_last_digits[0] * 10 + first_and_last_digits[1] 

for line_with_calibration_value in lines_with_calibration_values:
    val = get_calibration_value(line_with_calibration_value)
    calibration_values.append(val)

print(sum(calibration_values))