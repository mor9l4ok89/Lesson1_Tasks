summa = 0
count = 0
person = []
with open('salary.txt', 'r', encoding='utf-8') as f_obj:
    for sal in f_obj:
        sal = sal.split(' ')
        if int(sal[1]) < 20000:
            person.append(sal[0])
        summa += int(sal[1])
        count += 1
result = summa / count
print(f'Сотрудники, у кого оклад меньше 20000 - {person}')
print(f'Средний доход сотрудников - {result}')
