input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    dish = []
    for line in text:
        dish.append(list(line.strip()))
    return dish


def tilt_dish(dish, direction):
    tilted_dish = dish.copy()
    if direction in ('N', 'S'):
        if direction == 'S':
            bottom = len(tilted_dish)
            inc = -1
            ranges = reversed(range(len(tilted_dish[0])))
            dir_range = list(reversed(range(len(tilted_dish))))
        else:
            bottom = -1
            inc = 1
            ranges = range(len(tilted_dish[0]))
            dir_range = list(range(len(tilted_dish)))

        for x in ranges:
            cur_bottom = bottom
            for i in dir_range:
                # print(x, i, tilted_dish[i][x], bottom)
                if tilted_dish[i][x] == '#':
                    cur_bottom = i
                if tilted_dish[i][x] == 'O':
                    if i == cur_bottom + inc:
                        cur_bottom += inc
                        continue
                    tilted_dish[cur_bottom+inc][x] = 'O'
                    tilted_dish[i][x] = '.'
                    cur_bottom += inc
    if direction in ('W', 'E'):
        # Tilt north
        if direction == 'E':
            bottom = len(tilted_dish[0])
            inc = -1
            ranges = list(reversed(range(len(tilted_dish))))
            dir_range = list(reversed(range(len(tilted_dish[0]))))
        else:
            bottom = -1
            inc = 1
            ranges = list(range(len(tilted_dish)))
            dir_range = list(range(len(tilted_dish[0])))

        for i in ranges:
            cur_bottom = bottom
            for x in dir_range:
                # print(x, i, tilted_dish[i][x], bottom)
                # if i == 6:
                #     import pdb; pdb.set_trace()
                if tilted_dish[i][x] == '#':
                    cur_bottom = x
                if tilted_dish[i][x] == 'O':
                    if x == cur_bottom + inc:
                        cur_bottom += inc
                        continue
                    tilted_dish[i][cur_bottom+inc] = 'O'
                    tilted_dish[i][x] = '.'
                    cur_bottom += inc
    return tilted_dish


def calculate_load(dish):
    total = 0
    for i, load in enumerate(reversed(dish)):
        total += sum([i+1 for x in load if x == 'O'])
    return total


def run_simulation(dish, iters):
    tilted_dish = dish.copy()
    patterns = {}
    pattern_start = None
    i = 0
    while True:
        # import pdb; pdb.set_trace()
        pattern = hash(''.join([''.join([x for x in line]) for line in tilted_dish]))
        if pattern in patterns:
            pattern_start = patterns[pattern][1]
            pattern_end = i
            break
        result = calculate_load(tilted_dish)
        patterns[pattern] = (result, i)
        for d in ('N', 'W', 'S', 'E'):
            tilted_dish = tilt_dish(tilted_dish, d)
        i += 1

    pattern_buff = pattern_start
    final_pattern = [
        r[0] for pat, r in sorted(patterns.items(), key=lambda x: x[1][1])[pattern_start:pattern_end]
    ]

    run_idx = (iters - pattern_buff) % len(final_pattern)

    return final_pattern[run_idx]


def main():
    dish = parse_data(input_data)
    return run_simulation(dish, 1000000000)


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    pprint(result)