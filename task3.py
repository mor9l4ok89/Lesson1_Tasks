# Узнать у пользователя число n. И вывести сумму чисел в виде n + nn + nnn

n = int(input('Введите число: '))
nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)

print(n + int(nn) + int(nnn))

