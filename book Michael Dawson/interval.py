# Программа подсчета всех чисел в указанном интервале по срезу указанному ползоватлем

start = int(input('Введите начало счета: '))
finish = int(input('Введите конец счета: '))
interval = int(input('Введите интервал счета: '))
print('\nПосчитаем числа из введенного интервала по введенному счету: ')

for el in range(start, finish, interval):
    print(el, end=' ')
