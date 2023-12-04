valid_game_ids = []
required_solution = {
    'green': 13,
    'red': 12,
    'blue': 14
}

def is_ball_pick_valid(ball_pick: str):
    number_and_color = ball_pick.split(' ')
    return required_solution[number_and_color[1]] >= int(number_and_color[0])

def is_bag_draw_meeting_criteria(bag_draw: str):
    ball_picks = bag_draw.split(', ')
    return all(is_ball_pick_valid(x) for x in ball_picks)

def are_valid_game_draws(game: str):
    bag_draws = game.split('; ')
    return all(is_bag_draw_meeting_criteria(x) for x in bag_draws)

with open('input.txt', encoding="utf-8") as f:
    i = 1
    for line in f:
        splitted_string = line.split(': ')
        if are_valid_game_draws(splitted_string[1].strip('\n')):
            valid_game_ids.append(i)
        i += 1
                
f.closed

print(sum(valid_game_ids))