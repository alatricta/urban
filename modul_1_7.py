grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

result = {a: (sum(b)/len(b)) for a, b in zip(sorted(students), grades)}
# result = {a: b for a, b in zip(sorted(students), map(lambda x: sum(x) / len(x), grades))}

print(result)
