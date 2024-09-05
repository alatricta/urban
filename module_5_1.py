class House():
    def __init__(self, name, floors, cur_floor = 1):
        self.name = name
        self.number_of_floors = floors
        self.cur_floor = cur_floor
        
        
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