def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(5,5,5,5,7))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["add"])
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=10)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
