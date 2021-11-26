class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}!")

    def show_speed(self):
        print(f"Текущая скорость машины {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Осторожно! Скорость превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Осторожно! Скорость превышена!")


class PoliceCar(Car):
    is_police = True
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(61, "Коричневый", "Smart")
sport = SportCar(97, "Красный", "Lamborghini")
work = WorkCar(43, "Синий", "BMW")
police = PoliceCar(125, "Белый", "Ford")
work.go()
work.show_speed()
work.speed = 39
work.show_speed()
work.stop()
sport.turn("направо")
