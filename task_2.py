# Запрос у пользователя времени в секундах и вывод времени в формате чч:мм:сс

time_at_now = int(input('Введите время в секундах: '))

if time_at_now < 86400:
    time_in_hours = time_at_now // 3600
    time_in_minutes = (time_at_now - time_in_hours * 3600) // 60
    time_in_seconds = time_at_now - (time_in_hours * 3600 + time_in_minutes * 60)
    print(f"Введенное время в чч:мм:сс - {time_in_hours}:{time_in_minutes}:{time_in_seconds}")
else:
    time_in_days = (time_at_now // 86400) % 30
    time_in_hours = (time_at_now // 3600) % 24
    time_in_minutes = (time_at_now - time_in_hours * 3600) % 60
    time_in_seconds = (time_at_now - (time_in_hours * 3600 + time_in_minutes * 60)) % 86400
    print(f"Введенное время в дд:чч:мм:сс {time_in_days}:{time_in_hours}:{time_in_minutes}:{time_in_seconds}")

