
input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    times = int(''.join([x.strip()for x in text[0].split()[1:]]))
    distances = int(''.join([x.strip()for x in text[1].split()[1:]]))
    return times, distances


def calculate_distance(t, b, s):
    return (b * s) * (t - b)


def main():
    race_time, race_distance = parse_data(input_data)
    s = 1
    fails = 0
    for b in range(race_time + 1):
        calc_dist = calculate_distance(race_time, b, s)
        if calc_dist <= race_distance:
            fails += 1
        else:
            # break as soon as we beat distance
            break

    return race_time - (fails * 2) + 1


if __name__ == '__main__':
    print(main())

