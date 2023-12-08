input_file = 'input.txt'


with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    directions = text[0].strip()
    network = {}
    for line in text[1:]:
        if '=' not in line:
            continue
        key, values = line.split('=')
        key = key.strip()
        values = values.strip().replace('(', '').replace(')', '').split(',')
        network[key] = {'L': values[0].strip(), 'R': values[1].strip()}
    return directions, network


def main():
    directions, network = parse_data(input_data)
    current_step = 'AAA'
    end = 'ZZZ'
    steps = 0
    while True:
        next_direction = directions[steps % len(directions)]
        print(current_step, steps, next_direction)
        current_step = network[current_step][next_direction]
        steps += 1
        if current_step == end:
            break
    return steps


if __name__ == '__main__':
    print('Steps Taken to end:', main())