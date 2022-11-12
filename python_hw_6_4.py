class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go_car(self):
        print(f'Машина марки {self.name}, цвет {self.color}, поехала')

    def stop_car(self):
        print(f'Машина марки {self.name}, цвет {self.color}, остановилась')

    def turn_direction(self, direction):
        self.direction = direction
        print(f'Машина марки {self.name}, цвет {self.color}, повернула {self.direction}')

    def show_speed(self):
        print(f'Машина марки {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена (допустимая скорость не более 60 км/ч)')
        else:
            print(f'Машина марки {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена (допустимая скорость не более 40 км/ч)')
        else:
            print(f'Машина марки {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    def warning_police(self):
        if self.is_police == True:
            print(f'Это полицейская машина')
        else:
            print(f'Это не полиция')


a = TownCar(70, 'синий', 'jeep', False)
a.go_car()
a.stop_car()
a.turn_direction('на право')
a.show_speed()

b = PoliceCar(50, 'красный', 'BMW', False)
b.warning_police()
b.show_speed()
b.stop_car()

c = WorkCar(35, 'белый', 'Suzuki', False)
print(c.color)
c.show_speed()
c.turn_direction('назад')