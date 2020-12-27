
def delete(num_1, num_2):

    if num_1 == 0 or num_2 == 0:
        return 'Любое кроме ноля, нету деления на ноль.'
    else:
        return num_1 / num_2

print(delete(int(input('Введите число: ')),
             int(input('Введите число: '))))
