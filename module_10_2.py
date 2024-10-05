from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100 - self.power
        sleep(1)
        days = 1
        while enemy > 0:
            print(f'{self.name} сражается {days} день(дня), осталось {enemy} повергнуть воинов!')
            enemy -= self.power
            sleep(1)
            days += 1

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

def threads_start(threads):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


threads = []
threads.append(Knight('Брюс Ли', 10))
threads.append(Knight('Чак Норис', 20))
threads.append(Knight('КинКонг', 100))

threads_start(threads)
