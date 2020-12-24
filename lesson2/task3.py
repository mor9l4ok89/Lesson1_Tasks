
my_dict =  {1:'Январь',
            2:'Феварль',
            3:'Март',
            4:'Апрель',
            5:'Май',
            6:'Июнь',
            7:'Июль',
            8:'Август',
            9:'Сентябрь',
            10:'Октябрь',
            11:'Ноябрь',
            12:'Декабрь'}

my_list = ['Зиме', 'Весне', 'Лету', 'Осени']

key = int(input('Введите месяц в виде целого числа: '))

if key in my_dict:
    print(my_dict.get(key))
else:
    print('Такого месяца не существует')

if key == 1 or key == 2 or key == 12:
    print('Месяц относится к', my_list[0])
elif key == 3 or key == 4 or key == 5:
    print('Месяц относится к', my_list[1])
elif key == 6 or key == 7 or key == 8:
    print('Месяц относится к', my_list[2])
elif key == 9 or key == 10 or key == 11:
    print('Месяц относится к', my_list[3])
else:
    print('И не будет!)')
