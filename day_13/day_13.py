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
        if record[i] == record[i+1]:
            l = record[:i+1]
            r = record[i+1:]
            mirror_size = min(len(l), len(r))
            l = l[-mirror_size:]
            r = r[:mirror_size][::-1]
            # print(l)
            # print(r)
            if l == r:
                row_size = max(i+1, row_size)

    # check left to right
    transposed = [[record[x][y] for x in range(len(record))] for y in range(len(record[0]))]
    column_size = 0
    for i in range(len(transposed) - 1):
        if transposed[i] == transposed[i+1]:
            l = transposed[:i + 1]
            r = transposed[i + 1:]
            mirror_size = min(len(l), len(r))
            l = l[-mirror_size:]
            r = r[:mirror_size][::-1]
            # print(l)
            # print(r)
            if l == r:
                column_size = max(i + 1, column_size)

    return column_size + (row_size * 100)


def main():
    data = parse_data(input_data)
    total = 0
    i = 1
    for record in data:
        # pprint(record)
        reflection = find_mirror(record)
        print(i, reflection)
        total += reflection
        i += 1
    return total


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    print(result)