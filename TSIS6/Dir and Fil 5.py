def write_list_to_file(file_path, list_to_write):
    with open(file_path, 'w') as file:
        for item in list_to_write:
            file.write(f"{item}\\n")

example_list = ['apple', 'banana', 'cherry']

file_path = 'file.txt'

write_list_to_file(file_path, example_list)

print(f"Список успешно записан в файл '{file_path}'.")
