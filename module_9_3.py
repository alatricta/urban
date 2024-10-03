first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(a[0])-len(a[1]) for a in zip(first, second) if len(a[0]) != len(a[1]))
second_result = (len(first[i])==len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))