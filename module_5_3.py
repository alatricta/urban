class House():
    def __init__(self, name, floors, cur_floor = 1):
        self.name = name
        self.number_of_floors = floors
        self.cur_floor = cur_floor
        
        
    def __len__(self):
        return self.number_of_floors
        
        
    def __str__(self):
        return f'Название: {self.name}, '\
                f'кол-во этажей: {self.number_of_floors}'
                
    
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else: 
            return False
        
        
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else: 
            return None
        
        
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else: 
            return None
        
        
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else: 
            return None
        
        
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else: 
            return None
    
    
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else: 
            return None
    
    
    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        
        return self
        
    
    def __radd__(self, value):
        return self.__add__(value)
        
        
    def __iadd__(self, value):
        return self.__add__(value)
    
    
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует.')
        else:
            for i in range(new_floor):
                print(i + 1)
                self.cur_floor += 1
                
                
if __name__ == '__main__':
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
    
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    
    print('__str__')
    print(h1)
    print(h2)
    
    print('__len__')
    print(len(h1))
    print(len(h2))
    
    print('__eq__')
    print(h1 == h2)

    print('__add__')
    h1 = h1 + 10
    print(h1)
    print(h1 == h2)
    
    print('__iadd__')
    h1 += 10
    print(h1)
    
    print('__radd__')
    h2 = 10 + h2
    print(h2)
    
    print('__gt__', h1 > h2)
    print('__ge__', h1 >= h2)
    print('__lt__', h1 < h2)
    print('__le__', h1 <= h2)
    print('__ne__', h1 != h2)
    
    print('House + House')
    print(h1 + h2)
    print(h2 + h1)
    h1 += h2
    print(h1)