
proceeds = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
difference = proceeds - costs

if proceeds > costs:
    print('Вы работаете с прибылью ' + str(difference) + ', так держать!')
    print('Рентабельность работы фирмы: ' + str((difference/proceeds) * 100) + ' %')
    persons = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ' + str(((difference/proceeds) * 100) / persons) + ' %')
else:
    print('Вы работает в убыток на ' + str(-difference) + ', надо что то думать!')



