my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

print('FOR')
for d in my_list:
    if d > 0:
        print(d)
    elif d < 0:
        break

print('\nWHILE')
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break

    i +=1