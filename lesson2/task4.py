
phrase = input('Введите несколько слов: ')
my_list = phrase.split(' ')
i = 1

for element in my_list:
    if len(element) <= 9:
        print(f"{i} - {element}")
        i += 1
    else:
        print(phrase[0:10])
