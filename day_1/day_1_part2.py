import re

input_file = 'input_part2.txt'

nums = (
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
)

with open(input_file) as file:
    input_data = file.readlines()


def get_calib_value(text):
    """
    Loop through each number (0-9) and captures the indexes of each occurrence of it.
    The min and max indexes are identified as the first and last number found in the string
    and the calibration value is calculated from those.
    """
    num_idx = {}
    for str_num, int_num in nums:
        for idx in re.finditer(rf'({str_num})', text):
            num_idx[idx.start(1)] = int_num
    if not num_idx:
        return 0
    first_num = num_idx[min(num_idx)]
    last_num = num_idx[max(num_idx)]
    calib_value = int(first_num + last_num)
    return calib_value


def main():
    calib_values = []

    for line in input_data:
        calib_values.append(get_calib_value(line))

    return sum(calib_values)


if __name__ == '__main__':

    print(main())