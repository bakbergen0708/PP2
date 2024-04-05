def check_all_true(input_tuple):
    return all(input_tuple)

example_tuple = (True, True, True)

result = check_all_true(example_tuple)
print(f"Все элементы истинны в кортеже: {result}")
