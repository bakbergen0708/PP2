import shutil

def copy_file(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)
    print(f"Содержимое {source_path} было скопировано в {destination_path}")

source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

copy_file(source_file_path, destination_file_path)
