import sys

time, rate, prize = sys.argv

x = int(time)
v = int(rate)
c = int(prize)
# time = input(int('Введите значение: '))

# print('Имя скрипта: ', script_name)
# print('Параметр 1: ', time)
# print('Параметр 2: ', rate)
# print('Параметр 3: ', prize)

# def salary():

try:
    # x = int(time)
    # v = int(rate)
    # c = int(prize)
    sal = (x * v) + c
    print(f'Заработная плата: {sal}')
except ValueError:
    print('Введите корректные данные')

# print(salary())