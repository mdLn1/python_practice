lines = []
with open('input.txt', encoding="utf-8") as f:
    lines = f.readlines()

f.closed

line_length = len(lines[0])
adjacent_numbers = []
symbols = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>?/""")
for i in range(len(lines)):
    current_line = lines[i]
    j = 0
    while j < line_length:
        if current_line[j:j+1].isnumeric():
            
            is_adjacent = False
            found_number = int(current_line[j:j+1])
            
            if j > 0:
                if current_line[j-1] in symbols:
                    is_adjacent = True
            
            if i > 0:
                if lines[i-1][j-1] in symbols:
                    is_adjacent = True
            
            if i < len(lines) - 1:
                if lines[i+1][j-1] in symbols:
                    is_adjacent = True
            
            initial_j = j
            while current_line[initial_j:j+1].isnumeric() and j+1 < line_length:
                if not is_adjacent:
                    if i > 0:
                        if lines[i-1][j] in symbols:
                            is_adjacent = True
            
                    if i < len(lines) - 1:
                        if lines[i+1][j] in symbols:
                            is_adjacent = True

                found_number = int(current_line[initial_j:j+1])
                j += 1
            
            if not is_adjacent:
                if j < line_length:
                    if current_line[j] in symbols:
                        is_adjacent = True

                    if i > 0:
                        if lines[i-1][j] in symbols:
                            is_adjacent = True

                    if i + 1 < len(lines):
                        if lines[i+1][j] in symbols:
                            is_adjacent = True
                        
            if is_adjacent:
                adjacent_numbers.append(found_number)
        else:
            j += 1

print(adjacent_numbers)
print(sum(adjacent_numbers))