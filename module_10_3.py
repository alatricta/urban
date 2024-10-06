from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self) -> None:
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        transactions = 100
        for i in range(transactions):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            cash = randint(50, 500)
            self.balance += cash
            print(f'{i+1} - Пополнение: {cash}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        transactions = 100
        for i in range(transactions):
            cash = randint(50, 500)
            print(f'Запрос на {cash}')
            if cash <= self.balance:
                self.balance -= cash
                print(f'{i+1} - Снятие: {cash}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bank = Bank()
th1 = Thread(target=bank.deposit)
th2 = Thread(target=bank.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')
