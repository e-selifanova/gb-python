'''
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)


    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул вправо'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул влево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для городского автомобиля {self.name} {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше допустимого для городского автомобиля\n'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость для грузового автомобиля {self.name} {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше допустимого для грузового автомобиля\n'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} - полицейский'
        else:
            return f'Автомобиль {self.name} - не полицейский'

audi = SportCar(120, 'Черный', 'Ауди', '')
skoda = TownCar(75, 'Белый', 'Шкода', '')
scania = WorkCar(70, 'Желтый', 'Скания', '')
man = WorkCar(35, 'Красный', 'Ман', '')
bmw = PoliceCar(110, 'Черный', 'БМВ', '')

print(f'{audi.go()}')
print(f'{audi.show_speed()}')
print(f'{audi.turn_left()}')
print(f'{audi.turn_right()}')
print(f'{audi.stop()}\n')

print(f'{skoda.go()}')
print(f'{skoda.show_speed()}')

print(f'{scania.go()}')
print(f'{scania.show_speed()}')

print(f'{man.go()}')

print(f'{bmw.go()}')
print(f'{bmw.police()}')
