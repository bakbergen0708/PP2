def count_case(s):
    upper_case_count = 0
    lower_case_count = 0
    
    for char in s:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    
    return upper_case_count, lower_case_count

input_string = "Hello World!"

upper_count, lower_count = count_case(input_string)

print(f"В строке '{input_string}' содержится {upper_count} заглавных букв и {lower_count} строчных букв.")