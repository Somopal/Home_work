"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}.')

    def show_speed(self):
        return f'Скорость автомобиля {self.name}: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} превышена! Она составляет: {self.speed}'
        else:
            return f'Скорость {self.name} ОК'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} превышена! Она составляет: {self.speed}'
        else:
            return f'Скорость {self.name} ОК'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


print("\n")

town = TownCar(180, 'черный', 'BMW')
town.go()
town.stop()
town.turn("направо")
print(town.show_speed())

print("\n")

sport = SportCar(200, 'желтый', 'Audi')
sport.go()
sport.stop()
sport.turn("направо, а затем налево")
print(sport.show_speed())

print("\n")

work = WorkCar(40, 'синий', 'Hyundai')
work.go()
work.stop()
work.turn("налево, направо, а затем прямо, пока не доехал до дачи")
print(work.show_speed())

print("\n")

poloce = PoliceCar(120, 'белый', 'полиции')
poloce.go()
poloce.stop()
poloce.turn("налево")
print(poloce.show_speed())
