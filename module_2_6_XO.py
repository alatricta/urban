import os
from random import choice


def draw_area(area: list):
    intro = '''\
Добро пожаловать в игру Крестик Нолики!
Сначала указывается вертикальная координата (буква),
затем горизонтальная координата (цифра)
Для завершения игры нажмите "Q"
Приятной игры!'''
    top_line = '''\
     1     2     3
  ┌─────┬─────┬─────┐'''
    middle_line = '  ├─────┼─────┼─────┤'
    bottom_line = '  └─────┴─────┴─────┘'
    line1 = f'A │  {area[0][0]}  │  {area[0][1]}  │  {area[0][2]}  │'
    line2 = f'B │  {area[1][0]}  │  {area[1][1]}  │  {area[1][2]}  │'
    line3 = f'C │  {area[2][0]}  │  {area[2][1]}  │  {area[2][2]}  │'

    os.system('cls||clear')
    print(intro)
    print(top_line)
    print(line1)
    print(middle_line)
    print(line2)
    print(middle_line)
    print(line3)
    print(bottom_line)


def check_winner(area: list):
    winner_sequence = []
    winner_sequence.extend(area)
    winner_sequence.extend(list(zip(*area)))

    diagonal = [[], []]
    for i in range(3):
        diagonal[0].append(area[i][i])
        diagonal[1].append(area[i][-1-i])
    winner_sequence.extend(diagonal)

    for seq in winner_sequence:
        if seq == ['X','X','X']:
            print('Выиграли крестики')
            return True
        elif seq == ['0','0','0']:
            print('Выиграли нолики')
            return True
    else:
        return False


def analyze_step(step: str):
    step = step.strip().upper()
    if step == 'Q':
        quit()
        
    vertical = {'A':0, 'B':1, 'C':2}
    
    if len(step) != 2 or \
        step[0] not in vertical or \
        not step[1].isdigit() or \
        int(step[1]) > 3:
        return False
    
    coordinat = []
    coordinat.append(vertical[step[0]])
    coordinat.append(int(step[1])-1)
    return coordinat
    

def main():
    area = [[' ', ' ', ' '] for _ in range(3)]
    draw_area(area)

    match input('Кто начинает игру (1 - Крестики, 2 - Нолики, 3 - Случайно: '):
        case '1':
            gamer = 'X'
        case '2':
            gamer = '0'
        case _:
            gamer = choice(['X','0'])
    
    step = 1
    while not check_winner(area):
        if step > 9:
            print('Ничья!')
            break
        
        if gamer == 'X':
            print('Сейчас ходят Крестики.')
        else:
            print('Сейчас ходят Нолики.')
        
        gamer_step = input('Делайте ваш ход: ')
        gamer_step = analyze_step(gamer_step)
        if not gamer_step:
            continue
        elif area[gamer_step[0]][gamer_step[1]] != ' ':
            continue
        else:
            area[gamer_step[0]][gamer_step[1]] = gamer
        
        step += 1
        gamer = 'X' if gamer=='0' else '0'
        draw_area(area)


if __name__=='__main__':
    main()
