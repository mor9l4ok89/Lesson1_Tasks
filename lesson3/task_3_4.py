

def my_func(num_1, num_2):
    return num_1 ** abs(num_2)
print(my_func(int(input('Введите первое число: ')),
              int(input('Введите второе число: '))))

def my_func2(num1, num2):

    i = 1   # Степень
    result = 1
    while i <= num2:
        result *= num1
        i += 1
    print(result)

my_func2(int(input('Введите первое число: ')),
         int(input('Введите второе число: ')))