distance = int(input('Введите дистанцию первого забега: '))
distance_max = int(input('Введите максимальную дистанцую: '))
days = 1

while distance < distance_max:
    days += 1
    distance = distance + distance * 0.1

print('На ' + str(days) + '-й день спортсмен достиг результата - не менее ' + str(distance_max) + ' км.')

