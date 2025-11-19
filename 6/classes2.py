class Car:
    def __init__(self):
        self.__speed = 0

    @property
    def speed(self) -> int:
        return self.__speed


    def accelerate(self, x: int):
        if x >= 0:
            self.__speed += x

    def deaccelerate(self, x: int):
        if x >= 0:
            self.__speed = max(0, self.__speed - x)


aaaa = Car()

aaaa.accelerate(80)

