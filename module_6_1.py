class Plant:
    edible = False
    
    def __init__(self, name: str):
        self.name = name 


class Animal:
    alive = True
    fed = False    
    
    def __init__(self, name: str):
        self.name = name 
        
        
    def eat(self, food: Plant):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True 
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Meat(Plant):
    'Знаю что это не совсем правильно, просто экспиремент!'
    edible = True


class Mammal(Animal):
    pass 
    
    
class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Meat):
            print(f'{self.name} съел {food.name}, и облизнулся!')
            self.fed = True 
        else:
            super().eat(food)
    
    
    
class Flower(Plant):
    pass
    
    
class Fruit(Plant):
    edible = True


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    m1 = Meat('Кусок мяса')
    
    print(a1.name)
    print(p1.name)
    
    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
    a1.eat(m1)
    a2.eat(m1)
    print(a1.alive)
    print(a1.fed)
    print(a2.alive)
    print(a2.fed)