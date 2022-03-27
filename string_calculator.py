def add_string(string_numbers):
    if len(string_numbers)==0:
        return 0
    
    else:
        delimiter=','
        if string_numbers[0]=='/' and string_numbers[1]=='/':
            delimiter = string_numbers[2]
            string_numbers = string_numbers[4::]

        numbers_after_split = string_numbers.split(delimiter)
        negative=False
        negative_numbers=""
        for number in numbers_after_split:
            newline_split_number = number.split('\n')
            if len(newline_split_number)>1:
                if int(newline_split_number[0])<0:
                    negative=True
                    negative_numbers= negative_numbers+" "+newline_split_number[0]
                if int(newline_split_number[1])<0:
                    negative=True
                    negative_numbers= negative_numbers+" "+newline_split_number[1]
            elif int(number)<0:
                negative=True
                negative_numbers= negative_numbers+" "+number
        
        if negative:
            raise ValueError("negatives not allowed:"+negative_numbers)

        result = 0

        for number in numbers_after_split:
            newline_split_number = number.split('\n')
            if len(newline_split_number)>1:
                result += int(newline_split_number[0]) + int(newline_split_number[1])
            else:
                result += int(number)
        return result