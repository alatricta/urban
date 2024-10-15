import asyncio

cargo_count = 5
winners = []

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования!')
    
    for i in range(1, cargo_count+1):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар #{i}')

    winners.append(name)
    print(f'Силач {name} закончил соревнования.')    
    

def print_winners():
    print('='*15)
    print('Соревнование завершилось! Первые места:')

    for n in range(3):
        print(f'Место #{n+1} занял {winners[n]}')


async def start_tournament():
    strongmans = [('Vasya', 2), ('Fill', 3), ('Apollo', 5), ('Mark', 2), ('Alex', 2.3)]
    
    await asyncio.gather(*(start_strongman(*n) for n in strongmans))
    print_winners()

if __name__ == '__main__':
    asyncio.run(start_tournament())
