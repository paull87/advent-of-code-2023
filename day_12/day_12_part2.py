from functools import lru_cache

input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    return [
        (line.split()[0].strip(), [int(x) for x in line.split()[1].strip().split(',')]) for line in text
    ]


@lru_cache(maxsize=400)
def traverse_options(seq, expected, counts=None):
    # print('B', seq, expected, counts)
    # if seq == '#..###?#??.###????':
    #     import pdb; pdb.set_trace()
    counts = counts or 0
    idx = seq.index('?')
    for char in ('.', '#'):
        exp_copy = list(expected)
        failed_seq = False
        seq_split = list(seq)
        seq_split[idx] = char
        seq = ''.join(seq_split)
        # if seq == '.####.####.##?.?#':
        #     import pdb; pdb.set_trace()
        seq_chunks = [x for x in seq.split('.') if x]
        if list(seq).count('?') + list(seq).count('#') < sum(exp_copy):
            continue
        if list(seq).count('#') > sum(exp_copy):
            continue
        for chunk in seq_chunks:
            # if chunk == '#####?#?':
            #     import pdb; pdb.set_trace()
            # print('c', seq, exp_copy, counts, chunk)
            section = chunk.split('?')[0]
            if len(exp_copy) == 0 and '#' in chunk:
                failed_seq = True
                break
            elif len(exp_copy) == 0:
                break
            if len(section) == exp_copy[0]:
                exp_copy.pop(0)
            elif len(section) > exp_copy[0]:
                failed_seq = True
                break
            elif len(section) < exp_copy[0] and '?' not in chunk:
                failed_seq = True
                break
            elif len(section) < exp_copy[0]:
                break
            if len(exp_copy) == 0 and len([x for x in chunk.split('?')[1:] if x]) > 0 and '#' in section:
                failed_seq = True
                break
            if '?' in chunk:
                break
        # print('A', seq, exp_copy, counts, failed_seq)
        if failed_seq:
            continue
        # whole sequence is accounted for so stop there
        if len(exp_copy) == 0:
            # print('S', seq, expected, counts, failed_seq)
            counts += 1
        elif '?' not in seq:
            counts += 0
        else:
            counts = traverse_options(seq, expected, counts)

    return counts


def calculate_seq(seq, expected):
    exp_seq = [f"{'#' * x}" for x in expected]
    # print(seq, exp_seq)
    condensed_seq = '.'.join([x for x in seq.split('.') if x])
    exp_seq_str = '.'.join(exp_seq)
    # print(seq)
    # print(condensed_seq)
    # print(exp_seq_str)
    diff = len(condensed_seq) - len(exp_seq_str)
    if diff == 0:
        return 1
    return traverse_options(condensed_seq, expected)


def main():
    seqs = parse_data(input_data)
    possibles = []
    i = 0
    for seq, result in seqs:
        i += 1
        unfold_seq = '?'.join([seq] * 5)
        unfold_result = result * 5
        # if seq != '??##??????????.?#':
        #     continue
        # print(seq)
        # print(unfold_seq)
        # print(unfold_result)
        poss = calculate_seq(unfold_seq, tuple(unfold_result))
        print(f"{i} of {len(seqs)}")
        print(seq, result, poss)
        possibles.append(poss)
    return possibles


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    print(sum(result))

