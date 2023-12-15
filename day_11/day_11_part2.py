input_file = 'input.txt'

DRIFT = 1000000

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    return [[x for x in line.strip()] for line in text]


def apply_cosmic_drift(paths):
    columns = []
    rows = []

    # columns
    for i in range(len(paths[0])):
        column = [line[i] for line in paths]
        if set(column) == {'.'}:
            columns.append(i)

    # rows
    for i in range(len(paths)):
        if set(paths[i]) == {'.'}:
            rows.append(i)

    return columns, rows


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


def calculate_galaxy_distances(galaxies, columns, rows):
    pairs = {}
    for l in galaxies:
        for r in galaxies:
            pair = tuple(sorted((l, r)))
            if l == r or pair in pairs:
                continue
            l_pos = galaxies[l]
            r_pos = galaxies[r]
            distance = abs(l_pos[0] - r_pos[0]) + abs(l_pos[1] - r_pos[1])
            additional_drift = 0
            for r in rows:
                if l_pos[1] <= r <= r_pos[1] or r_pos[1] <= r <= l_pos[1]:
                    additional_drift += DRIFT - 1
            for c in columns:
                if l_pos[0] <= c <= r_pos[0] or r_pos[0] <= c <= l_pos[0]:
                    additional_drift += DRIFT - 1
            pairs[pair] = distance + additional_drift
    return pairs


def print_paths(paths):
    for line in paths:
        print(''.join(line))


def main():
    paths = parse_data(input_data)
    # print_paths(paths)
    columns, rows = apply_cosmic_drift(paths)
    paths, galaxies = number_galaxies(paths)
    galaxy_pairs = calculate_galaxy_distances(galaxies, columns, rows)
    return galaxy_pairs


if __name__ == '__main__':
    result = main()
    print(len(result))
    print(sum(result.values()))
    # print(result)
