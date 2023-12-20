input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    seq_steps = [x.strip() for x in ''.join([line.strip() for line in text]).split(',')]
    return seq_steps


def hash_alg(seq):
    alg = 0
    for c in seq:
        alg = ((alg + ord(c)) * 17) % 256
        # print(c, alg)
    return alg


def main():
    seq_steps = parse_data(input_data)
    total = []
    for step in seq_steps:
        # print(step, hash_alg(step))
        total.append(hash_alg(step))
    return sum(total)


if __name__ == '__main__':
    result = main()
    print(result)
