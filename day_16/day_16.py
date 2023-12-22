input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


DIRECTIONS = {
    'l': (-1, 0),
    'r': (1, 0),
    'u': (0, -1),
    'd': (0, 1),
}


def parse_data(text):
    layout = [list(line.strip()) for line in text]
    return layout


def print_layout(layout):
    for l in layout:
        print(''.join(l))


def create_beam_map(layout):
    return [[set() for _ in line] for line in layout]


def simulate_beam(layout, beam_layout):
    beams = [
        {'pos': (0, 0), 'direction': 'r'},
    ]
    while beams:
        del_beams = []
        new_beams = []
        # import pdb; pdb.set_trace()
        # print(beams)
        for i, beam in enumerate(beams):
            print(beam, len(layout), len(layout[0]))
            if 0 > beam['pos'][0] or beam['pos'][0] >= len(layout[0]):
                del_beams.append(i)
                continue
            if 0 > beam['pos'][1] or beam['pos'][1] >= len(layout):
                del_beams.append(i)
                continue
            dir = beam['direction']
            nx, ny = DIRECTIONS[dir]
            px, py = beam['pos']
            # if direction has already passed through, we can remove
            if dir in beam_layout[py][px]:
                del_beams.append(i)
                continue
            beam_layout[py][px].add(dir)
            cur_char = layout[py][px]
            if cur_char == '.':
                beam['pos'] = (px+nx, py+ny)
            elif cur_char == '-':
                if dir in ('l', 'r'):
                    beam['pos'] = (px+nx, py+ny)
                else:
                    # branch left and right
                    lx, ly = DIRECTIONS['l']
                    rx, ry = DIRECTIONS['r']
                    new_beams.append({'pos': (px+lx, py+ly), 'direction': 'l'})
                    new_beams.append({'pos': (px + rx, py + ry), 'direction': 'r'})
                    del_beams.append(i)
            elif cur_char == '|':
                if dir in ('u', 'd'):
                    beam['pos'] = (px+nx, py+ny)
                else:
                    # branch up and down
                    ux, uy = DIRECTIONS['u']
                    dx, dy = DIRECTIONS['d']
                    new_beams.append({'pos': (px+dx, py+dy), 'direction': 'd'})
                    new_beams.append({'pos': (px + ux, py + uy), 'direction': 'u'})
                    del_beams.append(i)
            elif cur_char == '/':
                new_dir = {
                    'u': 'r',
                    'd': 'l',
                    'l': 'd',
                    'r': 'u',
                }
                beam['direction'] = new_dir[dir]
                x, y = DIRECTIONS[beam['direction']]
                beam['pos'] = (px+x, py+y)
            elif cur_char == '\\':
                new_dir = {
                    'u': 'l',
                    'd': 'r',
                    'l': 'u',
                    'r': 'd',
                }
                beam['direction'] = new_dir[dir]
                x, y = DIRECTIONS[beam['direction']]
                beam['pos'] = (px + x, py + y)

        # remove redundant beams
        beams = [x for i, x in enumerate(beams) if i not in del_beams]
        # add new beams
        beams += new_beams


def beams_paths(beam_layout):
    return [['#' if x else '.' for x in line] for line in beam_layout]


def beam_power(beam_path):
    return sum([sum([1 for x in line if x == '#']) for line in beam_path])


def main():
    layout = parse_data(input_data)
    beam_layout = create_beam_map(layout)
    # pprint(beam_layout)
    simulate_beam(layout, beam_layout)
    beam_path = beams_paths(beam_layout)
    print('-------')
    print_layout(beam_path)
    print('-------')

    return beam_power(beam_path)


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    print(result)