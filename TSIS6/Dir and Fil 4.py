def count_lines(file_path):
    line_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    
    return line_count

file_path = 'file.txt'

print(f"Количество строк в файле: {count_lines(file_path)}")
