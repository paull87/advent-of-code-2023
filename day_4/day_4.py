
input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    cards = {}
    for line in text:
        card_name, numbers = line.split(':')
        card_name = card_name.strip()
        numbers = numbers.strip()
        picks_str, winners_str = numbers.split('|')
        picks = [int(x.strip()) for x in picks_str.split()]
        winners = [int(x.strip()) for x in winners_str.split()]
        cards[card_name] = {
            'picks': picks,
            'winners': winners,
        }
    return cards


def determine_winnings(card):
    winning_nums = set(card['picks']).intersection(set(card['winners']))
    points = 0
    # print(winning_nums, len(winning_nums))
    if len(winning_nums) > 0:
        points = 2 ** (len(winning_nums) - 1)
    return points


def main():
    cards = parse_data(input_data)
    total_points = 0
    for card_name, card in cards.items():
        card_points = determine_winnings(card)
        print(f'{card_name}: {card_points}')
        total_points += card_points
    return total_points


if __name__ == '__main__':
    print(main())