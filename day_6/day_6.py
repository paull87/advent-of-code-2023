
input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    times = [int(x.strip()) for x in text[0].split()[1:]]
    distances = [int(x.strip()) for x in text[1].split()[1:]]
    races = list(zip(times, distances))
    return races


def calculate_distance(t, b, s):
    return (b * s) * (t - b)


def main():
    races = parse_data(input_data)
    s = 1
    result = 1
    for race in races:
        margin = 0
        race_time = race[0]
        race_distance = race[1]
        for b in range(race_time + 1):
            calc_dist = calculate_distance(race_time, b, s)
            if calc_dist > race_distance:
                margin += 1
        result *= margin

    return result


if __name__ == '__main__':
    print(main())

