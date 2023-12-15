input_file = 'input.txt'


START = 'S'

DIRECTION_MAP = {
    START: [
        (0, -1),
        # (-1, -1),
        (-1, 0),
        # (-1, 1),
        (0, 1),
        # (1, 1),
        (1, 0),
        # (1, -1),
    ],
    '|': [
        (0, 1),
        (0, -1),
    ],
    '-': [
        (1, 0),
        (-1, 0),
    ],
    'L': [
        (0, -1),
        (1, 0),
    ],
    'J': [
        (-1, 0),
        (0, -1),
    ],
    '7': [
        (0, 1),
        (-1, 0),
    ],
    'F': [
        (0, 1),
        (1, 0),
    ]
}

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    return [[x.strip() for x in line.strip()] for line in text]


class Mapper:
    def __init__(self, directions):
        self.directions = directions
        self.moves = self.copy_empty_directions()
        self.start_pos = self.find_start()
        self.moves[self.start_pos[1]][self.start_pos[0]] = 0

    def copy_empty_directions(self):
        return [['.' for _ in y] for y in self.directions]

    def find_start(self):
        for y in range(len(self.directions)):
            for x in range(len(self.directions[0])):
                if self.directions[y][x] == START:
                    return x, y

    def export_map(self, maps):
        with open('test.csv', 'w') as text_file:
            for m in maps:
                text_file.write(','.join([str(x) for x in m]) + '\n')

    def print_map(self, maps):
        for m in maps:
            print(' '.join([str(x) for x in m]))

    def next_moves(self, x, y):
        current_char = self.directions[y][x]
        return[(x + m[0], y + m[1]) for m in DIRECTION_MAP.get(current_char, [])]

    def find_starting_moves(self):
        valid_starts = []
        for move in self.next_moves(*self.start_pos):
            if self.start_pos in self.next_moves(*move):
                valid_starts.append(move)
        return valid_starts

    def check_valid_move(self, pot_pos, steps):
        if not 0 <= pot_pos[1] < len(self.directions):
            return False
        if not 0 <= pot_pos[0] < len(self.directions[0]):
            return False
        if self.directions[pot_pos[1]][pot_pos[0]] not in DIRECTION_MAP:
            return False
        if self.moves[pot_pos[1]][pot_pos[0]] != '.':
            return False
        # if steps + 1 <= int(str(self.moves[pot_pos[1]][pot_pos[1]]).replace('.', '-1')):
        #     return False
        return True

    def run(self):
        self.print_map(self.directions)
        moves = self.find_starting_moves()
        steps = 0
        while moves:
            steps += 1
            # if steps == 5:
            #     import pdb; pdb.set_trace()
            print(moves)
            next_moves = []
            for move in moves:
                # if move == (3, 0):
                #     import pdb; pdb.set_trace()
                if self.check_valid_move(move, steps):
                    next_moves += self.next_moves(move[0], move[1])
                    self.moves[move[1]][move[0]] = steps
            # self.print_map(self.moves)
            moves = next_moves
        self.export_map(self.moves)
        return steps - 1


def main():
    directions = parse_data(input_data)
    mapper = Mapper(directions)
    return mapper.run()


if __name__ == '__main__':
    from pprint import pprint
    print('Steps taken:', main())