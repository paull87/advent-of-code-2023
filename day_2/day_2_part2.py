
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


def calculate_powers(game):
    power = 1
    for count in game.values():
        power *= count
    return power


def main():
    games = parse_games()
    game_limits = {}
    for game, turns in games.items():
        game_limit = {}
        for turn in turns:
            for colour, count in turn.items():
                game_limit[colour] = max(game_limit.get(colour, 0), count)

        game_limits[game] = game_limit

    powers = [calculate_powers(x) for x in game_limits.values()]
    return powers


if __name__ == '__main__':
    result = main()
    print(result)
    print(sum(result))
