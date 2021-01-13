# Только согласные
# Программа демонстрирует, как создавать новые строки из исходных с помощью цикла for

message = input('Введите текст: ')
new_message = ""
vowels = "aeiouаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print('Создана новая строка: ', new_message)
print('\nВот ваш текст с изъятыми гласными буквами: ', new_message)
