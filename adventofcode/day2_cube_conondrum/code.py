valid_games = []
with open('input.txt', encoding="utf-8") as f:
    for line in f:
        splitted_string = line.split(':')
        game_number = int(splitted_string[0][5:])
        bag_draws = splitted_string[1].split(';')
f.closed

print(valid_games)