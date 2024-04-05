def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = "A man a plan a canal Panama"

result = is_palindrome(input_string)

print(f"Строка '{input_string}' является палиндромом: {result}.")