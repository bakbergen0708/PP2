from functools import reduce

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers_list = [1, 2, 3, 4, 5]

result = multiply_numbers(numbers_list)
print(f"Результат умножения всех чисел в списке {numbers_list} равен {result}.")