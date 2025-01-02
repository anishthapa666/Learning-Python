class Car:
    def __init__(self,model,power,is_for_sale):
        self.model= model
        self.power= power
        
        self.is_for_sale= is_for_sale

    # def get_model(self):
    #     return self.__model
    
    # @staticmethod
    # def car_key():
    #     return "its working properly"

    # @property
    # def get_power(self):
    #     return self.__power

c1 = Car("appache","550 hp",True)

# print(c1.model)
class Condition(Car):
    def __init__(self,is_safe,model,power,is_for_sale):
        super().__init__(model,power,is_for_sale)
        self.is_safe = is_safe

class Repair(Car):
    def __init__(self,model,power,is_for_sale,time):
        super().__init__(model,power,is_for_sale)
        self.time = time

c2 = Repair("pulsar","220",True,"1hr")
print(c2.time)