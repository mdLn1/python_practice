total_points = 0
lines = []
with open('input.txt', encoding="utf-8") as f:
    for line in f:
        game_number,card_content = line.rstrip('\n').split(':')
        winning, drawn = card_content.split('|')
        drawn_numbers = set([x for x in drawn.split(' ') if x])
        winning_numbers = dict([[x, x] for x in winning.split(' ') if x])
        winning_cases = sum([1 for x in drawn_numbers if winning_numbers.get(x, 0)])
        lines.append([1, winning_cases])

f.closed

for i in range(len(lines)):
    scratchcard_values = lines[i]
    if scratchcard_values[1] > 0:
        temp = i + 1
        while temp <= min(i + scratchcard_values[1], len(lines) - 1):
            val = lines[temp]
            lines[temp] = [val[0] + scratchcard_values[0], val[1]]
            temp += 1
    total_points += scratchcard_values[0]

print(total_points)
