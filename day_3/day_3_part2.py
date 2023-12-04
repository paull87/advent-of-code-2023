expected_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
gear_symbol = '*'

input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def data_to_array(text):
    return [[x for x in y.strip()] for y in text]


def find_gear_numbers(array, gears):
    gear_output = {}
    for x, y in gears:
        # check above
        checks = {(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)}
        # check below
        checks = checks.union({(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)})
        # check left and right
        checks = checks.union({(x, y - 1), (x, y + 1)})
        # find numbers
        gear_nums = []
        already_a_num = []
        for c_x, c_y in checks:
            # check that number hasn't already been accounted for
            if (c_x, c_y) in already_a_num:
                continue
            number = ''
            num_co_ords = []
            if array[c_y][c_x] in expected_numbers:
                number = array[c_y][c_x]
                num_co_ords.append((c_x, c_y))
                # check left of number
                l_x = c_x
                while True:
                    l_x -= 1
                    if not 0 <= l_x < len(array[0]):
                        break
                    if array[c_y][l_x] in expected_numbers:
                        number = array[c_y][l_x] + number
                        num_co_ords.append((l_x, c_y))
                    else:
                        break
                # check right of number
                r_x = c_x
                while True:
                    r_x += 1
                    if not 0 <= r_x < len(array[0]):
                        break
                    if array[c_y][r_x] in expected_numbers:
                        number += array[c_y][r_x]
                        num_co_ords.append((r_x, c_y))
                    else:
                        break
            if number:
                gear_nums.append((number, num_co_ords))
                already_a_num.extend(num_co_ords)
        if len(gear_nums) == 2:
            gear_output[(x, y)] = gear_nums
    # print(gear_output)
    return gear_output


def find_gears(array):
    co_ords = []
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == gear_symbol:
                co_ords.append((x, y))
    return co_ords


def main():
    array = data_to_array(input_data)
    gears = find_gears(array)
    # print(gears)
    gear_nums = find_gear_numbers(array, gears)
    result = 0
    for gear, nums in gear_nums.items():
        gear_ratio = int(nums[0][0]) * int(nums[1][0])
        result += gear_ratio
    return result


if __name__ == '__main__':
    result = main()
    print(result)
