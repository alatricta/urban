def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        d = 2
        while result % d != 0:
            d += 1
        if d == result:
            print('Простое')
        else:
            print('Составное')
        
        return result
    return wrapper
    
@is_prime
def sum_three (a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)
result = sum_three(10, 3, 8)
print(result)