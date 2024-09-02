def get_numbers(n: int|str) -> str:
    try:
        n = int(n)
    except:
        print('Введено не число!')
        quit()
        
    if n < 3 or n > 20:
        print('Введено недопустимое число!')
        quit()
    
    s = ''
    for i in range(1, n):
        for j in range(i+1, n-i+1):
            tmp = i + j 
            if n % tmp == 0:
                s += ''.join(map(str, (i,j)))
    return s
    
    
if __name__ == '__main__':
    num = input('Введите число: ')
    print(get_numbers(num))