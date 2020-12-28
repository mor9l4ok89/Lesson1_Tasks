
def my_func():
    numbers = input('Введите числа через пробел:').split()
    sum = 0
    for num in numbers:
        sum += int(num)
    return sum

print(my_func())

try:
    if num == num.isalpha():
        print('Ваша сумма - {}, функция завершается'.format(sum))
        break
except:
    print('Ваша сумма - {}, функция продолжается'.format(sum))
    continue