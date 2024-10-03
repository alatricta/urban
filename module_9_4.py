# lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda a,b: a==b, first, second)))

# loopback
def get_advanced_writer(file_name):
    
    def write_everything(*data_set):
        with open(file_name, 'w') as f:
            for data in data_set:
                f.write(f'{data}\n')
                
    return write_everything
    
writer = get_advanced_writer('example.txt')
writer('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt') as f:
    print(f.read())

   
# __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words if self.__is_valid_words(words) else ()
        
    def __is_valid_words(self, words):
        if not words:
            raise ValueError('Список не должен быть пустым')
            
        for word in words:
            if not isinstance(word, str):
                raise ValueError('Неверный тип данных')
                
        return True

    def __call__(self):
        from random import choice
        return choice(self.words)
        
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())