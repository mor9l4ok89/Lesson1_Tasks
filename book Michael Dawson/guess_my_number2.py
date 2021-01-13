import random

print('\tДобро пожаловать в игру "Отгадай число"!')
print('\nЯ постараюсь отгадать число из диапазона от 1 до 100.\n')


guess = int(input('Загадайте мне число от 1 до 100: '))
tries = 1
while tries != 6:
    number = random.randint(1, 100)
    if guess == number:
        print(f'Вот правильное число - {guess}')
    elif number > guess:
        input(f'Это верное число? - {number}, если нет, то нажмите Enter.')
    else:
        input(f'Может быть это верное число? - {number} если нет, то продолжим, нажмите Enter.')
    tries += 1

print('К сожалению я не отгадал')