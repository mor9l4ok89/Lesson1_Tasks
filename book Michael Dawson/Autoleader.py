car = float(input('Введите стоимость автомобиля - '))
nalog = car * 0.1
cbor = car * 0.05
agent_cbor = 500
dostavka = 1000

car_price = car + nalog + cbor + agent_cbor + dostavka

print('\nОкончательная сумма вашего авто с учетом всех налогов и сборов - ', car_price)
