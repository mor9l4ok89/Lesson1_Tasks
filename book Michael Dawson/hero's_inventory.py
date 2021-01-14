# Арсенал героя
# Демонстрирует создание кортежа
# Создадим пустой кортеж
inventory = ()
# Рассмотрим его как условие
if not inventory:
    print('Вы безоружны!')
input('\nНажмите Enter, для создания арсенала.')
# Теперь создадим кортеж с несколькими элементами
inventory = ('Меч',
             'Кольчуга',
             'Щит',
             'Целебный элексир')
# Выведем этот кортеж на экран
print('\nСодержимое арсенала.')
print(inventory)
# Выведем все элементы последовательно
print('\nИтак, в вашем арсенале: ')
for item in inventory:
    print(item)
# Найдем длину кортежа
print('\nСейчас в вашем распоряжении ', len(inventory), ' предмета(ов).')
input('\nНажмите Enter, чтобы продолжить.')
# Проверка принадлежности кортежу при помощи in
if 'Целебный элексир' in inventory:
    print('Вы еще поживете и повоюете.')
# вывод одного элемента с определенным индексом
index = int(input('\nВведите индекс одного из предметов арсенала: '))
print('Под индексом ', index, ' в арсенале находится ', inventory[index])
# Отобразим срез
start = int(input('\nВведите начальный индекс среза: '))
finish = int(input('Введите конечный индекс среза: '))
print('Срез inventory[ ', start, ':', finish, '] - это', end=' ')
print(inventory[start:finish])
input('\nНажмите Enter, чтобы продолжить.')
# Соединим два кортежа, так как кортежи НЕИЗМЕНЯЕМЫ
chest = ('Золото', 'Драгоценные камни')
print('Вы нашли ларец, вот что в нем есть:')
print(chest)
print('Вы приобщили содержимое ларца к своему арсеналу.')
inventory += chest
print('Теперь в вашем распоряжении:')
print(inventory)
input('\nНажмите Enter, чтобы выйти.')