
def my_func(num_1, num_2, num_3):
    if num_1 >= num_3 and num_2 >= num_3:
        return num_1 + num_2
    elif num_1 < num_2 and num_1 < num_3:
        return num_2 + num_3
    else:
        return num_3 + num_1

print(my_func(int(input(('Введите первое число: '))),
              int(input(('Введите второе число: '))),
              int(input(('Введите третье число: ')))))