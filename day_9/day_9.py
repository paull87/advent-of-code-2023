input_file = 'input.txt'


with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    return [[int(x.strip()) for x in line.strip().split()] for line in text]


def find_next_value(sequence):
    results = [sequence.copy()]
    while set(results[-1]) != {0}:
        curr_seq = results[-1]
        next_seq = [curr_seq[i+1] - curr_seq[i] for i in range(len(curr_seq)-1)]
        results.append(next_seq)

    for i in reversed(range(1, len(results))):
        results[i-1].append(results[i][-1] + results[i-1][-1])

    # for line in results:
    #     print(*(f'{x}' for x in line))
    return results[0][-1]


def main():
    sequences = parse_data(input_data)
    next_values = []
    for sequence in sequences:
        next_values.append(find_next_value(sequence))
    print(next_values)
    return sum(next_values)


if __name__ == '__main__':
    print(main())