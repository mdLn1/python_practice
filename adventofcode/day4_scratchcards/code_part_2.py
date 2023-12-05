total_points = 0
lines = []
with open('input.txt', encoding="utf-8") as f:
    for line in f:
        game_number,card_content = line.rstrip('\n').split(':')
        winning, drawn = card_content.split('|')
        drawn_numbers = [x for x in drawn.split(' ') if x]
        winning_numbers = dict([[x, x] for x in winning.split(' ') if x])
        winning_cases = sum([1 for x in drawn_numbers if winning_numbers.get(x, 0)])
        if winning_cases > 0:
            winning_cases = 1
        lines.append([1, winning_cases])

f.closed
for i, scratchcard_values in enumerate(lines):
    if scratchcard_values[1] > 0:
        temp = i + 1
        while temp < i + scratchcard_values[1] and temp < len(lines) - 1:
            val = lines[temp]
            lines[temp] = [val[0] + 1, val[1]]
    total_points += scratchcard_values[0]

print(total_points)
