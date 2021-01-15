with open('summ.txt', 'w', encoding='utf-8') as f_obj:
    try:
        my_list = input('Введите несколько чисел через пробел: ')
        f_obj.write(my_list)
        i = my_list.split(' ')
        print(sum(map(int, i)))
    except ValueError:
        print('Ошибка ввода данных.')
