from collections import OrderedDict
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


def process_step(step, boxes):
    if step.endswith('-'):
        label = step.split('-')[0]
        action = 'remove'
    else:
        label, lens = step.split('=')
        action = 'add'
    alg_idx = hash_alg(label)
    # print(label, lens, alg_idx, action)
    if action == 'add':
        boxes[alg_idx][label] = int(lens)
    else:
        boxes[alg_idx].pop(label, None)


def calculate_focus_power(boxes):
    total = []
    for ib, box in enumerate(boxes):
        for i, space in enumerate(box.items()):
            total.append(((ib + 1) * (i + 1)) * space[1])

    return total

def main():
    seq_steps = parse_data(input_data)
    boxes = [OrderedDict() for _ in range(256)]
    print(boxes)
    total = []
    for step in seq_steps:
        # print(step, hash_alg(step))
        process_step(step, boxes)
        total.append(hash_alg(step))
        # print(boxes[:4])
    power = calculate_focus_power(boxes)
    print(power)
    return sum(power)


if __name__ == '__main__':
    result = main()
    print(result)
