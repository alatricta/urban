def print_params(a = 1, b = 'строка', c = True):
    print('Параметр а:', a)
    print('Параметр b:', b)
    print('Параметр c:', c)
    print('-'*25)
    
    
    
if __name__ == '__main__':
    print_params()
    print_params(a=4)
    print_params(b=True, c = False)
    print_params(b = 25)
    print_params(c = [1,2,3])
    
    values_list = [True, 55.34, 'PruBet']
    print_params(*values_list)
    
    values_dict = {'a':125, 'b':False, 'c':6.72}
    print_params(**values_dict)
    
    values_list_2 = [True, 5.45]
    print_params(*values_list_2, 42)
    