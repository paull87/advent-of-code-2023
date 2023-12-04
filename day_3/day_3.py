import numpy

expected_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def data_to_array(text):
    return [[x for x in y.strip()] for y in text]


def find_numbers(array):
    numbers = []
    for y in range(len(array)):
        number = ''
        co_ords = []
        for x in range(len(array[y])):
            if array[y][x] in expected_numbers:
                number += array[y][x]
                co_ords.append((x, y))
            else:
                if number:
                    numbers.append((int(number), co_ords.copy()))
                    number = ''
                    co_ords = []
        if number:
            numbers.append((int(number), co_ords.copy()))
    return numbers


def check_for_valid_number(array, co_ords):
    checks = set()
    for x, y in co_ords:
        print(x, y)
        # check above
        checks = checks.union({(x-1, y-1), (x-1, y), (x-1, y+1)})
        # check below
        checks = checks.union({(x+1, y-1), (x+1, y), (x+1, y+1)})
        # check left and right
        checks = checks.union({(x, y-1), (x, y+1)})
    for x, y in checks:
        if 0 < x < len(array[0]) and 0 < y < len(array):
            if array[y][x] not in expected_numbers + ['.']:
                return True


def main():
    array = data_to_array(input_data)
    all_numbers = find_numbers(array)
    valid_nums = []
    for num, co_ords in all_numbers:
        if check_for_valid_number(array, co_ords):
            valid_nums.append(num)
    return valid_nums


if __name__ == '__main__':
    from pprint import pprint
    result = main()
    pprint(result)
    print(sum(result))
