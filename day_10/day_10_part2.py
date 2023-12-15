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

    def find_start(self, maps=None):
        maps = maps or self.directions
        for y in range(len(maps)):
            for x in range(len(maps[y])):
                if maps[y][x] == START:
                    return x, y

    def export_map(self, maps):
        with open('test_overlay.csv', 'w') as text_file:
            for m in maps:
                text_file.write(','.join([str(x) for x in m]) + '\n')

    def print_map(self, maps):
        for m in maps:
            print(' '.join([str(x) for x in m]))

    def overlay_map(self):
        lines = []
        for y in range(len(self.directions)):
            line = []
            for x in range(len(self.directions[0])):
                line.append(self.moves[y][x] if self.moves[y][x] in ('I', 'O') else self.directions[y][x])
            lines.append(line)
        self.export_map(lines)

    def next_moves(self, x, y, maps=None):
        maps = maps or self.directions
        current_char = maps[y][x]
        return[(x + m[0], y + m[1]) for m in DIRECTION_MAP.get(current_char, [])]

    def find_starting_moves(self, pos=None):
        pos = pos or self.start_pos
        valid_starts = []
        for move in self.next_moves(*pos):
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

    def find_empty_space(self, maps=None):
        maps = maps or self.moves
        for y in range(len(maps)):
            for x in range(len(maps[0])):
                if str(maps[y][x]) == '.':
                    return x, y

    def all_neighbours(self, x, y, maps=None):
        maps = maps or self.moves
        neighbours = []
        available = [
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        for n_x, n_y in available:
            if not 0 <= y + n_y < len(maps):
                continue
            if not 0 <= x + n_x < len(maps[0]):
                continue
            neighbours.append((x + n_x, y + n_y))
        return neighbours

    def count_loop_area(self, maps=None):
        maps = maps or self.moves
        return sum([sum([1 for x in y if str(x) == 'I']) for y in maps])

    def expand_map(self):
        new_map = self.directions.copy()
        # import pdb;pdb.set_trace()
        for y in range(1, (len(new_map) * 2)-1, 2):
            new_map.insert(y, ['.' for _ in range(len(new_map[0]))])
        for y in range(len(new_map)):
            for x in range(1, (len(new_map[y]) * 2) - 1, 2):
                new_map[y].insert(x, '.')
        # connect pipes
        for y in range(0, len(new_map), 2):
            for x in range(0, len(new_map[y]), 2):
                char = new_map[y][x]
                if char == '-':
                    if x > 0 and new_map[y][x-2] in ('F', 'L', '-'):
                        new_map[y][x-1] = '-'
                    if x < len(new_map[y])-1 and new_map[y][x+2] in ('7', 'J', '-'):
                        new_map[y][x+1] = '-'
                if char == '|':
                    if y > 0 and new_map[y-2][x] in ('F', '7', '|'):
                        new_map[y-1][x] = '|'
                    if y < len(new_map)-1 and new_map[y+2][x] in ('L', 'J', '|'):
                        new_map[y+1][x] = '|'
                if char == 'F':
                    if x < len(new_map[y])-1 and new_map[y][x+2] in ('J', '7', '-'):
                        new_map[y][x+1] = '-'
                    if y < len(new_map)-1 and new_map[y+2][x] in ('L', 'J', '|'):
                        new_map[y+1][x] = '|'
                if char == '7':
                    if x > 0 and new_map[y][x-2] in ('L', 'F', '-'):
                        new_map[y][x-1] = '-'
                    if y < len(new_map)-1 and new_map[y+2][x] in ('L', 'J', '|'):
                        new_map[y+1][x] = '|'
                if char == 'J':
                    if x > 0 and new_map[y][x-2] in ('L', 'F', '-'):
                        new_map[y][x-1] = '-'
                    if y > 0 and new_map[y-2][x] in ('F', '7', '|'):
                        new_map[y-1][x] = '|'
                if char == 'L':
                    if x < len(new_map[y]) - 1 and new_map[y][x + 2] in ('J', '7', '-'):
                        new_map[y][x + 1] = '-'
                    if y > 0 and new_map[y-2][x] in ('F', '7', '|'):
                        new_map[y-1][x] = '|'

        start_x, start_y = self.find_start(new_map)
        # top
        if start_y > 0:
            if (start_x, start_y - 1) in self.next_moves(start_x, start_y - 2, new_map):
                new_map[start_y-1][start_x] = '|'
        # bottom
        if start_y + 1 < len(new_map):
            if (start_x, start_y + 1) in self.next_moves(start_x, start_y + 2, new_map):
                new_map[start_y+1][start_x] = '|'
        # left
        if start_x > 0:
            if (start_x - 1, start_y) in self.next_moves(start_x - 2, start_y, new_map):
                new_map[start_y][start_x - 1] = '-'
        # right
        if start_y + 1 < len(new_map[0]):
            if (start_x + 1, start_y) in self.next_moves(start_x + 2, start_y, new_map):
                new_map[start_y][start_x + 1] = '-'
        self.print_map(new_map)
        return new_map

    def reduce_map(self, maps):
        maps = maps.copy()
        for y in reversed(range(1, len(maps), 2)):
            maps.pop(y)
        for y in range(len(maps)):
            for x in reversed(range(1, len(maps[y]), 2)):
                maps[y].pop(x)
        return maps

    def find_loop_area(self):
        expanded_map = self.expand_map()
        import pdb; pdb.set_trace()
        empty_space = self.find_empty_space(expanded_map)
        current_spaces = [empty_space]
        while True:
            next_spaces = []
            for space in current_spaces:
                # Already processed
                if expanded_map[space[1]][space[0]] == 'O':
                    continue
                neighbours = self.all_neighbours(*space, expanded_map)
                neighbour_values = [expanded_map[y][x] for x, y in neighbours]
                if len(neighbours) < 8:
                    expanded_map[space[1]][space[0]] = 'O'
                elif 'O' in neighbour_values:
                    expanded_map[space[1]][space[0]] = 'O'
                else:
                    expanded_map[space[1]][space[0]] = 'I'
                for neigh in neighbours:
                    # if neigh == (27, 19):
                    #     import pdb; pdb.set_trace()
                    if expanded_map[neigh[1]][neigh[0]] == '.':
                        next_spaces.append(neigh)
                    elif expanded_map[space[1]][space[0]] == 'O' and expanded_map[neigh[1]][neigh[0]] == 'I':
                        next_spaces.append(neigh)
            current_spaces = set(next_spaces)
            if not current_spaces:
                empty_space = self.find_empty_space(expanded_map)
                if empty_space:
                    current_spaces = [empty_space]
                else:
                    break
        self.export_map(expanded_map)
        final_map = self.reduce_map(expanded_map)
        # self.print_map(final_map)
        return self.count_loop_area(final_map)


    def run(self):
        # self.print_map(self.directions)
        moves = self.find_starting_moves()
        steps = 0
        while moves:
            steps += 1
            # if steps == 5:
            #     import pdb; pdb.set_trace()
            # print(moves)
            next_moves = []
            for move in moves:
                # if move == (3, 0):
                #     import pdb; pdb.set_trace()
                if self.check_valid_move(move, steps):
                    next_moves += self.next_moves(move[0], move[1])
                    self.moves[move[1]][move[0]] = steps
            # self.print_map(self.moves)
            moves = next_moves
        return steps - 1



def main():
    directions = parse_data(input_data)
    mapper = Mapper(directions)
    print('Steps taken:', mapper.run())
    print('Loop area:', mapper.find_loop_area())


if __name__ == '__main__':
    from pprint import pprint
    main()