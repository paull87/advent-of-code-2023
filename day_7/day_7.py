
input_file = 'input.txt'

CARD_ORDERS = {
    '5OK': 'A',
    '4OK': 'B',
    'FH': 'C',
    '3OK': 'D',
    '2P': 'E',
    '1P': 'F',
    'A': 'G',
    'K': 'H',
    'Q': 'I',
    'J': 'J',
    'T': 'K',
    '9': 'L',
    '8': 'M',
    '7': 'N',
    '6': 'O',
    '5': 'P',
    '4': 'Q',
    '3': 'R',
    '2': 'S',
}

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    games = [
        (x.split()[0].strip(), int(x.split()[1].strip())) for x in text
    ]
    return games


def score_hand(hand):
    # five of a kind
    score = ''
    unique_hand = list(set(hand))
    # import pdb; pdb.set_trace()
    if len(unique_hand) == 1:
        score += CARD_ORDERS['5OK']
    if len(unique_hand) == 2:
        # four of kind
        if len(hand.replace(unique_hand[0], '')) == 1 or len(hand.replace(unique_hand[1], '')) == 1:
            score += CARD_ORDERS['4OK']
        # full house
        elif len(hand.replace(unique_hand[0], '')) in (2, 3) and len(hand.replace(unique_hand[1], '')) in (2, 3):
            score += CARD_ORDERS['FH']
    if len(unique_hand) == 3:
        # 3 of kind
        if len(hand.replace(unique_hand[0], '')) == 2 or len(hand.replace(unique_hand[1], '')) == 2 or len(hand.replace(unique_hand[2], '')) == 2:
            score += CARD_ORDERS['3OK']
        # 2 pair
        else:
            score += CARD_ORDERS['2P']
    # pair
    if len(unique_hand) == 4:
        score += CARD_ORDERS['1P']

    for card in hand:
        score += CARD_ORDERS[card]

    return score


def main():
    games = parse_data(input_data)
    total_winnings = 0
    for rank, hand in enumerate(sorted(games, key=lambda x: score_hand(x[0]), reverse=True)):
        winnings = (rank + 1) * hand[1]
        total_winnings += winnings
        print(rank + 1, hand[0], hand[1], winnings)
        # print(hand[0], score_hand(hand))
    print(total_winnings)


if __name__ == '__main__':
    main()