# from itertools import count

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if el != el + 1]
print(f'Исходный список - {my_list}')
print(f'Новый список - {new_list}')
# for el in my_list.count(1):
#     if el ==