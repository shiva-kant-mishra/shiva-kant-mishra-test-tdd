def add_string(string_numbers):
    if len(string_numbers)==0:
        return 0
    elif len(string_numbers.split(","))==1:
        return int(string_numbers)
    else:
        numbers_after_split = string_numbers.split(",")
        result = 0
        for number in numbers_after_split:
            result += int(number)
        return result