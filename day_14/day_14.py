input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    dish = []
    for line in text:
        dish.append(list(line.strip()))
    return dish


def tilt_dish(dish):
    tilted_dish = dish.copy()
    # Go down each column
    for x in range(len(tilted_dish[0])):
        bottom = -1
        for i in range(len(tilted_dish)):
            # print(x, i, tilted_dish[i][x], bottom)
            # if x == 1:
            #     import pdb; pdb.set_trace()
            if tilted_dish[i][x] == '#':
                bottom = i
            if tilted_dish[i][x] == 'O':
                if i == bottom + 1:
                    bottom += 1
                    continue
                tilted_dish[bottom+1][x] = 'O'
                tilted_dish[i][x] = '.'
                bottom += 1
    return tilted_dish


def calculate_load(dish):
    total = 0
    for i, load in enumerate(reversed(dish)):
        total += sum([i+1 for x in load if x == 'O'])
    return total


def main():
    dish = parse_data(input_data)
    # pprint(dish)
    tilted = tilt_dish(dish)
    return calculate_load(tilted)


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    pprint(result)