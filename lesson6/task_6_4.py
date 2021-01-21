class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn_right(self):
        return f'{self.name} поворот направо.'

    def turn_left(self):
        return f'{self.name} поворот налево'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городской машины {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости, {self.name}, для городской машины.'
        else:
            return f'Скорость, {self.name}, можно и побыстрее.'

class SportCar(Car):
    pass
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Обычная скорость рабочей машины {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена, помедленее.'
        else:
            return f'Скорость {self.name}, можно поднажать!'


class PoliceCar(Car):
    pass
    # def __init__(self, speed, color, name, is_police):
    #     super().__init__(speed, color, name, is_police)
    #
    # def police(self):
    #     if self.is_police:
    #         return f'{self.name} is from police department'
    #     else:
    #         return f'{self.name} is not from police department'

sport_car = SportCar(240, 'Красный', 'Мустанг', False)
town_car = TownCar(140, 'Белая', 'Шкода', False)
work_car = WorkCar(90, 'Синяя', 'Тойота', False)
police_car = PoliceCar(210, 'Цветная', 'Нива', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn_left()
sport_car.turn_right()
