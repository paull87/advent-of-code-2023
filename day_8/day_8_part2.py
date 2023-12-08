from math import lcm

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


def find_starting_steps(network):
    return [x for x in network.keys() if x[-1] == 'A']


def check_all_end_nodes(steps):
    return all([x[-1] == 'Z' for x in steps])


# Brute force did not work....
def _main():
    directions, network = parse_data(input_data)
    current_steps = find_starting_steps(network)[1:2]
    end = 'ZZZ'
    steps = 0
    while True:
        next_direction = directions[steps % len(directions)]
        print(current_steps)
        for i in range(len(current_steps)):
            print(current_steps[i], steps, next_direction)
            current_steps[i] = network[current_steps[i]][next_direction]
        steps += 1
        if check_all_end_nodes(current_steps):
            print(current_steps)
            break
    return steps


def find_loop(step, directions, network):
    current_steps = step
    steps = 0
    while True:
        next_direction = directions[steps % len(directions)]
        # print(current_steps)
        # print(current_steps[i], steps, next_direction)
        current_steps = network[current_steps][next_direction]
        steps += 1
        if current_steps[-1] == 'Z':
            return steps


def main():
    directions, network = parse_data(input_data)
    current_steps = find_starting_steps(network)
    steps = 0
    all_loops = []
    for starting_step in current_steps:
        print('Finding loops for:', starting_step)
        all_loops.append(find_loop(starting_step, directions, network))
    return lcm(*all_loops)


if __name__ == '__main__':
    print('Steps Taken to end:', main())