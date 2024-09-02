calls = 0 
calls_func = {'string_info':0,
              'is_contains':0}


def count_calls(func: str) -> list:
    global calls_func, calls 
    calls += 1 
    calls_func[func] += 1 
    
    
def string_info(string: str) -> tuple:
    count_calls('string_info')
    return len(string), string.upper(), string.lower()
    
    
def is_contains(string: str, list_:list ) -> bool:
    list_ = map(lambda s: s.lower(), list_)
    count_calls('is_contains')
    return string.lower() in list_
    
    
if __name__ == '__main__':
    lst = ['qwErty', 'tYpO', 'ganGUMstyle', 'FIGaro' ]
    print(string_info('gdgytr'))
    print(string_info('gdgytr'))
    print(is_contains('typo', lst))
    print(string_info('gdgytr'))
    print(is_contains('zaVtra', lst))
    
    print('Общее количество вызовов:', calls )
    print('Количество вызовов функции string_info:', calls_func['string_info'] )
    print('Количество вызовов функции is_contains:', calls_func['is_contains'] )
    