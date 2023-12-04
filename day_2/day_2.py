
game_limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_games():
    games = {}
    for line in input_data:
        game_name, game_turns = line.split(':')
        game_name = int(game_name.split()[1].strip())
        all_turns = []
        for turn in game_turns.strip().split(';'):
            all_turns.append({x.split()[1].strip(): int(x.split()[0].strip()) for x in turn.split(',')})
        games[game_name] = all_turns

    return games


def main():
    games = parse_games()
    invalid_games = []
    for game, turns in games.items():
        for turn in turns:
            for colour, limit in game_limits.items():
                if turn.get(colour, 0) > limit:
                    invalid_games.append(game)

    valid_games = list(set(games.keys()) - set(invalid_games))
    return valid_games


if __name__ == '__main__':
    result = main()
    print(result)
    print(sum(result))
