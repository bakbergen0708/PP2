import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            return f"Файл '{file_path}' был удален."
        else:
            return f"Доступ запрещен: Невозможно удалить файл '{file_path}'."
    else:
        return f"Файл не существует: '{file_path}'."

path_to_delete = 'path_to_your_file.txt'
print(delete_file(path_to_delete))
