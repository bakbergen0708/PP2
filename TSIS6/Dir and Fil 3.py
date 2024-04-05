import os

def check_path(path):
    if os.path.exists(path):
        directory_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        return True, directory_name, file_name
    else:
        return False, None, None

given_path = ' '

path_exists, directory, filename = check_path(given_path)

if path_exists:
    print(f"Путь существует.\nКаталог: {directory}\nИмя файла: {filename}")
else:
    print("Путь не существует.")
