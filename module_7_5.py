import time
import os


# Вывод заголовока ---->
file = 'Обнаружен файл:'
filepath = 'Путь:'
filesize = 'Размер:'
formatted_time = 'Время изменения:'
parent_dir = 'Родительская директория:'
print(f'{file:^25}'
      f'|{filepath:^40}'
      f'|{filesize:^12}'
      f'|{formatted_time:^25}'
      f'|{parent_dir:^30}')
# <---- Вывод заголовока

directory = '.'
for root, dirs, files in os.walk(directory):
    if '.' not in os.path.abspath(root) and \
       '__' not in os.path.abspath(root):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'{file:<25}'
                  f'|{filepath:<40}'
                  f'|{filesize:^12}'
                  f'|{formatted_time:^25}'
                  f'|{parent_dir:<30}')
