def calculate_structure_sum(*args):
    sum = 0
    for data in args:
        if isinstance(data, list | tuple | set):
            sum += calculate_structure_sum(*data)
        elif isinstance(data, dict):
            sum += calculate_structure_sum(*data.values())
            sum += calculate_structure_sum(*data.keys())
        elif isinstance(data, str):
            sum += len(data)
        elif isinstance(data, int):
            sum += data
            
    return sum
    
    
    
    
if __name__ == '__main__':
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
        ]
    result = calculate_structure_sum(data_structure)
    print(result)
