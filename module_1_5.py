immutable_var = (1, 2, 3, 4, 5, 'строка', True, [3, 2, 1])
print(immutable_var)

try:
    immutable_var[1] = 1000
except:
    print('Не сработало, потому что "tuple" - это неизменяемый тип данных')
    

mutable_list = list(immutable_var)
mutable_list[1] = 1000
print(mutable_list)
