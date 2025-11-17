class car():
    def __init__(self, brand, model):
        self.brand = brand
        self.date = model
    def give(self):
        print(self.brand)
        print(self.model)


class student():
    def __init__(self, index_number, name):
        self.name = name
        self.index_number = index_number

    def drinkBeer(self):
        print(f"{self.name} is drinking beer...")

class Rectangle():    

    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh
        # num_of_rectangle += 1

    def __str__(self):
        return f"Rectangle {self.width}x{self.heigh}"


class BankAccount():
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"Available: {self.saldo}"

    def withdraw(self, value):
        if value > self.saldo:
            print("Insufficient fundsz")
        else:
            self.saldo -= value
            print(f"Nowe saldo: {self.saldo}")

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) == int:
            return Vector2D(self.x + other, self.y + other)
        else:
            return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        return((self.x == other.x) and (self.y == other.y))


def main():
    Adam = student(2137, "Adam")
    Adam.drinkBeer()
    samochod1 = car("porsche", 2025)
    samochod2 = car("fiat", 1999)
    samochod3 = car("mercedes", 2005)
    num_of_rectangle = 0
    # pros1 = Rectangle(12,15)
    # pros2 = Rectangle(8,10)
    # print(f"{pros1.heigh}, {pros1.width}, {pros1.num_of_rectangle}")
    # print(f"{pros2.heigh}, {pros2.width}, {pros2.num_of_rectangle}")
    aaa = BankAccount(4000)
    aaa.withdraw(400)
    aaa.withdraw(9000)
    print(aaa)
    rec1 = Rectangle(200,400)
    print(rec1)
    p = Vector2D(3,4)
    z = p + 10
    print(z)
if __name__ == "__main__":
    main()