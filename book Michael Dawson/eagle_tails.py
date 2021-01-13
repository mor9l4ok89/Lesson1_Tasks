# Программа орел/решка
# Нужно случайным образом выбирать орла или решку
# Циклом вывести результат 100 раз

import random

orel = 0
resh = 0
count = 0
while count != 100:
    mon = random.randint(1, 2)
    count += 1
    if mon == 1:
        orel += 1

    elif mon == 2:
        resh += 1

print("Орел выпал", orel)
print("Решка выпала", resh)