# Создание файла и строк в нем
print('Создаю текстовый файл методом writelines().')
text_file = open('write_in.txt', 'w', encoding='utf-8')
text_file.write('Строка 1\n')
text_file.write('Это строка 2\n')
text_file.write('Этой строе достался номер 3\n')
text_file.close()

print('\nЧитаю вновь созданный файл.')
text_file = open('write_in.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()

print('\nСоздаю текстовый файл методом writelines().')
text_file = open('write_in.txt', 'w', encoding='utf-8')
lines = ['Строка 1\n',
         'это строка 2\n',
         'а это строка 3\n']
text_file.writelines(lines)
text_file.close()

print('\nЧитаем что наделали')
text_file = open('write_in.txt', 'r', encoding='utf-8')
print(text_file.read())
text_file.close()
input('\nНажмите Enter для выхода.')
