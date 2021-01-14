# Программа подсчета строк и слов

with open('for_task_2.txt', encoding='utf-8') as f_obj:
    content = f_obj.read().split()
    print(len(content))

with open('for_task_2.txt', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(len(content))
