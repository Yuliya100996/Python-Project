import os
import time
print(os.getcwd())

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime('%d,%m,%Y,%H,%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file},\n'
              f'путь: {filepath},\n'
              f'размер: {filesize},\n'
              f'время изменения: {formatted_time},\n'
              f'родительская директория: {parent_dir}')