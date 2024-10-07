from random import randint
from threading import Thread
from queue import Queue
from time import sleep


class Table:
    def __init__(self, number: int, guest=None) -> None:
        self.number = number
        self.guest = guest

    def __bool__(self):
        return bool(self.guest)


class Guest(Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables: Table) -> None:
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                
    def discuss_guests(self):
        while not self.queue.empty() or any(self.tables):
            for table in self.tables:
                if table.guest is None:
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest.start()
                elif not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                
                
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()