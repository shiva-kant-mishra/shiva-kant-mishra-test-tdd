def add_string(string_numbers):
    if len(string_numbers)==0:
        return 0
    elif len(string_numbers.split(","))==1:
        return int(string_numbers)
    else:
        numbers_after_split = string_numbers.split(",")
        return int(numbers_after_split[0]) + int(numbers_after_split[1])