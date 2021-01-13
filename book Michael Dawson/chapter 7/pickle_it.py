# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки
import pickle, shelve

print('Консервация списков.')
variety = ['Огурцы', 'Помидоры', 'Капуста']
shape = ['Целые', 'Кубиками', 'Соломкой']
brand = ['Главпродукт', 'Чумак', 'Бондюэль']
# Теперь открою на запись новый файл
f = open('pickles1.dat', 'wb')
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('\nРасконсервация списков.\n')
f = open('pickles1.dat', 'rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print('\nПомещение списков на полку.\n')
s = shelve.open('pickles2.dat')
s['variety'] = ['Огурцы', 'Помидоры', 'Капуста']
s['shape'] = ['Целые', 'Кубиками', 'Соломкой']
s['brand'] = ['Главпродукт', 'Чумак', 'Бондюэль']
s.sync()

print('\nИзвлечение списков из файла "полки".\n')
print('Торговые марки -', s['brand'])
print('Формы -', s['shape'])
print('Виды овощей -', s['variety'])
# Наконец закроем файл
s.close()
input('\nНажмите Enter для выхода.')
