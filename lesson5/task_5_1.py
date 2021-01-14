# Программа создания текстового файла, записи построчных данных от пользователя

text_file = open('Write_it.txt', 'w', encoding='utf-8')
answer = input('Введите текст - ')

while answer:
    text_file.write(answer)
    answer = input('Введите текст - ')
    if not answer:
        break
text_file.close()

text_file = open('Write_it.txt', 'r')
print(text_file.read())
text_file.close()

# with open('Write_it.txt') as f_obj:
#
# answer = input('Введите текст-')
#     if answer != '':
#         f_obj.write(answer)
#     else:
#         print('Вы ввели неверное значение.')
# # f_obj.close()

