# Словарь
my_dict = {1000: ('Alex', 1993), 1003: ('Ivan', 2000)}

existing_key = my_dict.get(1000)
unexisting_key = my_dict.get('Alex', 'Такого ключа не должно было быть, а ты ищешь!')


print('Начальный словарь:', my_dict)
print('Существующий ключ:', existing_key)
print('Несуществующий ключ:', unexisting_key)

my_dict[1536] = ('Vasya', 1995)
my_dict[1835] = ('Masha', 2003)

deleted_value = my_dict.pop(1835)
print('Удалённое значение:', deleted_value)

print('Конечный словарь:', my_dict)

# Множество
print('#'*15)
my_set = set([1,2,3,'text', 5, 1, 2, 3])
print('Начальное множество:', my_set)
my_set.add(45)
my_set.update({69, 'two'})
my_set.remove(2)
print('Конечное множество:', my_set)
