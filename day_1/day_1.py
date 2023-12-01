import re

input_file = 'input.txt'

with open(input_file) as file:
    input_data = file.readlines()


def get_calib_value(text):
    nums = re.sub(r"[^0-9]", "", text)
    if nums == "":
        return 0
    calib_value = int(nums[0] + nums[-1])
    return calib_value


def main():
    calib_values = []

    for line in input_data:
        calib_values.append(get_calib_value(line))

    return sum(calib_values)


if __name__ == '__main__':

    print(main())