NUMERIC_UNICODE_RANGE = (48, 57)


def get_calibration_values(calibration_file_path: str) -> list[int]:
    """
    Open a calibration txt file and retrieve the values for each line. Return these calibration
    values as a list of integers.
    """
    calibration_values = []

    with open(calibration_file_path, "r") as calibration_text:
        for line in calibration_text:
            calibration_values.append(retrieve_calibration_value_from_string(line))

    return calibration_values


def retrieve_calibration_value_from_string(line: str) -> int:
    """
    Calibration value is found by combining the first digit and the last digit in a string of
    numerical and non-numerical characters. Left and right pointers are used to scan the string
    from each end for the first and last interger, respectively.

    For example, 'ag5fh581nf12' will return 52.
    """
    l, r = 0, len(line) - 1
    l_found, r_found = False, False

    while l <= r:
        if is_character_numeric(line[l]):
            l_found = True
        else:
            l += 1
        if is_character_numeric(line[r]):
            r_found = True
        else:
            r -= 1

        if l_found and r_found:
            return int(line[l] + line[r])

    raise Exception("Two integers not found in string")


def is_character_numeric(char: str) -> bool:
    return NUMERIC_UNICODE_RANGE[0] <= ord(char) <= NUMERIC_UNICODE_RANGE[1]


if __name__ == "__main__":
    file_path = "./day_1/calibration.txt"
    calibration_values = get_calibration_values(file_path)
    calibration_sum = sum(calibration_values)

    print(f"The sum of all the calibration values is {calibration_sum}")
