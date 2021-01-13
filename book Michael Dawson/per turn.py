# Текст наоборот
text = input('Введите несколько слов: ')
my_list = []
for el in text[::-1]:
    my_list += el
    print(my_list)
