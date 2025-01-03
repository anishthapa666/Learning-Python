class Car:
    total_car = 0
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1
    def fuel_type(self):
        return "petrol or diesal "
    def get_brand(self):
        return self.__brand
    def set_brand(self,value):
        self.__brand= value
    def display(self):
        return f"{self.brand} {self.model}"
    @staticmethod
    def car_function():
        return "wow what a stufff"
class ElectricCar(Car):
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
    def fuel_type(self):
        return "electic charge"



my_tesla = ElectricCar("Tesla","Model 3","2000 kwh")
my_car = Car("pulsar","NS")
# print(my_car.brand)

# print(my_tesla.display())

# print(my_tesla.__brand)
# print(my_car.get_brand())

my_car.set_brand("nano")
print(my_car.get_brand())
print(my_tesla.fuel_type())
print(Car.total_car)
print(my_car.car_function())
