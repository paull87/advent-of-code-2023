
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
    # print(winning_nums)
    return len(winning_nums)


def main():
    cards = parse_data(input_data)
    winning_multi = [1] * len(cards)
    for i, card_name in enumerate(cards):
        card = cards[card_name]
        card_points = determine_winnings(card)
        multi = winning_multi[i]
        for m in range(card_points):
            next_idx = i+m+1
            if next_idx < len(winning_multi):
                winning_multi[next_idx] += multi
        # print(f'{card_name}: {card_points}')
        # print(winning_multi)
    return winning_multi


if __name__ == '__main__':
    result = main()
    print(result)
    print(sum(result))