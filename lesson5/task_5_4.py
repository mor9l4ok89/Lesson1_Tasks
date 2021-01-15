rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_rus = []
with open('for_task_4.txt', 'r', encoding='utf-8') as f_obj:
    for el in f_obj:
        el = el.split(' ', 1)
        new_rus.append(rus[el[0]] + '  ' + el[1])
    print(new_rus)

with open('for_task_4_new.txt', 'w', encoding='utf-8') as f_obj_2:
    f_obj_2.writelines(new_rus)