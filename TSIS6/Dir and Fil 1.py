import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

path = ' '

directories = list_directories(path)
print(f"Каталоги в '{path}': {directories}")

files = list_files(path)
print(f"Файлы в '{path}': {files}")

all_items = list_all(path)
print(f"Все каталоги и файлы в '{path}': {all_items}")
