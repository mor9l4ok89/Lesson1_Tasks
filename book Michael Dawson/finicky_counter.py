# Считалка
# Демонстрирует работ команд break и continue
count = 0
while True:
    count += 1
    # Завершить цикл, если каунт принимает значение больше 10
    if count > 10:
        break
    # пропустить 5
    if count == 5:
        continue
    print(count)
input('\nДля выхода из программы нажмите Enter.')