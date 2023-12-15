input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    return [[x for x in line.strip()] for line in text]


def apply_cosmic_drift(paths):
    # rows
    new_paths = paths.copy()

    # columns
    for i in reversed(range(len(new_paths[0]))):
        column = [line[i] for line in new_paths]
        if set(column) == {'.'}:
            for r in new_paths:
                r.insert(i, '.')

    for i in reversed(range(len(new_paths))):
        if set(new_paths[i]) == {'.'}:
            new_paths.insert(i, new_paths[i])

    return new_paths


def number_galaxies(paths):
    i = 1
    galaxies = {}
    numbered_paths = paths.copy()
    for y in range(len(paths)):
        for x in range(len(paths[y])):
            if paths[y][x] == '#':
                numbered_paths[y][x] = str(i)
                galaxies[i] = (x, y)
                i += 1

    return numbered_paths, galaxies


def calculate_galaxy_distances(galaxies):
    pairs = {}
    for l in galaxies:
        for r in galaxies:
            pair = tuple(sorted((l, r)))
            if l == r or pair in pairs:
                continue
            l_pos = galaxies[l]
            r_pos = galaxies[r]
            distance = abs(l_pos[0] - r_pos[0]) + abs(l_pos[1] - r_pos[1])
            pairs[pair] = distance
    return pairs


def print_paths(paths):
    for line in paths:
        print(''.join(line))


def main():
    paths = parse_data(input_data)
    # print_paths(paths)
    # print('------')
    paths = apply_cosmic_drift(paths)
    paths, galaxies = number_galaxies(paths)
    # print_paths(paths)
    galaxy_pairs = calculate_galaxy_distances(galaxies)
    return galaxy_pairs


if __name__ == '__main__':
    result = main()
    print(len(result))
    print(sum(result.values()))
    # print(result)
