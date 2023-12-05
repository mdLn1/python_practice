total_points = 0
with open('input.txt', encoding="utf-8") as f:
    for line in f:
        game_number,card_content = line.rstrip('\n').split(':')
        winning, drawn = card_content.split('|')
        drawn_numbers = [x for x in drawn.split(' ') if x]
        winning_numbers = dict([[x, x] for x in winning.split(' ') if x])
        winning_cases = sum([1 for x in drawn_numbers if winning_numbers.get(x, 0)])
        if winning_cases > 0:
            total_points += pow(2, winning_cases - 1)

f.closed
print(total_points)
