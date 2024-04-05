import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    return exists, readable, writable, executable

path_to_check = ' '

exists, readable, writable, executable = check_access(path_to_check)

print(f"Путь: {path_to_check}")
print(f"Существует: {'Да' if exists else 'Нет'}")
print(f"Читаемый: {'Да' if readable else 'Нет'}")
print(f"Записываемый: {'Да' if writable else 'Нет'}")
print(f"Исполняемый: {'Да' if executable else 'Нет'}")
