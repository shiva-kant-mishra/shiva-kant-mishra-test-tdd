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
                for num in newline_split_number:
                    if int(num) < 0:
                        negative=True
                        negative_numbers= negative_numbers+" "+num
                
            elif int(number)<0:
                negative=True
                negative_numbers= negative_numbers+" "+number
        
        if negative:
            raise ValueError("negatives not allowed:"+negative_numbers)

        result = 0

        for number in numbers_after_split:
            newline_split_number = number.split('\n')
            if len(newline_split_number)>1:
                for num in newline_split_number:
                    result+= int(num)
            else:
                result += int(number)
        return result