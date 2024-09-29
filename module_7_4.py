def main():
    team1_name = 'Мастера кода'
    team2_name = 'Волшебники данных'
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    # tasks_total = 82
    # time_avg = 45.2
    # challenge_result = 'Победа команды Волшебники данных!'

    def print_res():
        if (score_1 > score_2) or (score_1 == score_2 and team1_time < team2_time):
            challenge_result = f'Победа команды {team1_name}!'
        elif (score_1 < score_2) or (score_1 == score_2 and team1_time > team2_time):
            challenge_result = f'Победа команды {team2_name}!'
        else:
            challenge_result = 'Ничья!'

        tasks_total = score_1 + score_2
        # time_avg = max(team1_time, team2_time) / tasks_total
        time_avg = (team1_time + team2_time) / tasks_total

        print('\n# Использование %')
        print('В команде %(t1)s участников: %(t2)s!' % {'t1': team1_name, 't2': team1_num})
        print('В команде %(t1)s участников: %(t2)s!' % {'t1': team2_name, 't2': team2_num})
        print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

        print('\n# Использование format')
        print('Команда {} решила задач: {}!'.format(team1_name, score_1))
        print('{n} решили задачи за {t} с!'.format(t=team1_time, n=team1_name))
        print('Команда {} решила задач: {}!'.format(team2_name, score_2))
        print('{n} решили задачи за {t} с!'.format(t=team2_time, n=team2_name))

        print('\n# Использование f-строк')
        print(f'Команды решили {score_1} и {score_2} задач.')
        print(f'Результат битвы: {challenge_result}!')
        print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')

    print_res()


if __name__ == "__main__":
    main()
