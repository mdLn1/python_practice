default_ball_pick_dict = {
        'green': 0,
        'blue': 0,
        'red': 0
    }

total_sum = 0

def get_bag_draw_cubes(bag_draw: str):
    ball_picks = bag_draw.split(', ')
    ball_pick_dict = default_ball_pick_dict.copy()
    for x in ball_picks:
        [number, color] = x.split(' ')
        ball_pick_dict[color] = int(number)
    return ball_pick_dict

def get_minimum_game_color_coded_cubes(game: str):
    bag_draws = game.split('; ')
    minimum_game_balls = default_ball_pick_dict.copy()
    for x in bag_draws:
        bag_draw_cubes = get_bag_draw_cubes(x)
        for key, val in bag_draw_cubes.items():
            if minimum_game_balls[key] < val:
                minimum_game_balls[key] = val
    return minimum_game_balls

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

with open('input.txt', encoding="utf-8") as f:
    for line in f:
        splitted_string = line.split(': ')
        minimum_game_balls = get_minimum_game_color_coded_cubes(splitted_string[1].strip('\n'))
        result = multiplyList(minimum_game_balls.values())
        total_sum += result

f.closed

print(total_sum)