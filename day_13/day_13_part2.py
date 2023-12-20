input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def parse_data(text):
    records = []
    record = []
    for line in text:
        row = list(line.strip())
        if row:
            record.append(row)
        else:
            records.append(record.copy())
            record.clear()
    if record:
        records.append(record.copy())
    return records


def find_mirror(record):
    # check top to bottom
    row_size = 0
    for i in range(len(record)-1):
        smudge_used = False
        l_i, r_i = i, i + 1
        while True:
            l = record[l_i]
            r = record[r_i]
            if l == r:
                l_i -= 1
                r_i += 1
            elif not smudge_used:
                smudge_check = [idx for idx in range(len(l)) if l[idx] != r[idx]]
                if len(smudge_check) == 1:
                    change_idx = smudge_check[0]
                    l[change_idx] = r[change_idx]
                    smudge_used = True
                    l_i -= 1
                    r_i += 1
                else:
                    break
            else:
                break

            if (l_i < 0 or r_i >= len(record)) and smudge_used:
                row_size = max(i + 1, row_size)
                print('row', i + 1)
                break
            elif l_i < 0 or r_i >= len(record):
                break

    # check left to right
    transposed = [[record[x][y] for x in range(len(record))] for y in range(len(record[0]))]
    column_size = 0
    for i in range(len(transposed) - 1):
        smudge_used = False
        l_i, r_i = i, i + 1
        while True:
            l = transposed[l_i]
            r = transposed[r_i]
            if l == r:
                l_i -= 1
                r_i += 1
            elif not smudge_used:
                smudge_check = [idx for idx in range(len(l)) if l[idx] != r[idx]]
                if len(smudge_check) == 1:
                    change_idx = smudge_check[0]
                    l[change_idx] = r[change_idx]
                    smudge_used = True
                    l_i -= 1
                    r_i += 1
                else:
                    break
            else:
                break

            if (l_i < 0 or r_i >= len(transposed)) and smudge_used:
                print('column', i + 1)
                column_size = max(i + 1, column_size)
                break
            elif l_i < 0 or r_i >= len(transposed):
                break

    return max(column_size, row_size * 100, 1)


def main():
    data = parse_data(input_data)
    total = 0
    i = 1
    for record in data:
        pprint(record)
        reflection = find_mirror(record)
        print(i, reflection)
        total += reflection
        i += 1
    return total


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    print(result)