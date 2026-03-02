# from abc import ABC, abstractmethod
#
# class Cars(ABC):
#     def __init__(self,name,price,color):
#         self.name = name
#         self.price = price
#         self.color = color
#     @abstractmethod
#     def introduce(self):
#         pass
#
# class SportCar(Cars):
#     def __init__(self,name,price,color, turbo):
#         super().__init__(name, price, color)
#         self.turbo = turbo
#     def introduce(self):
#         return f"""
# Car name is {self.name}
# Price is {self.price}
# Color is {self.color}
# Turbo is {self.turbo}
# """
#
# class ElectricCar(Cars):
#     def __init__(self,name,price,color, battery):
#         super().__init__(name, price, color)
#         self.__battery = battery
#
#     @property
#     def battery(self):
#         return {self.__battery}
#     @battery.setter
#     def battery(self,battery):
#         self.__battery = battery
#         return self.__battery
#
#     def introduce(self):
#         return f"""
# Name is {self.name}
# Price is {self.price}
# Color is {self.color}
# Battery is {self.__battery}
# """
#
# sport_car = SportCar("Bugatti",200_000,"blue", 100)
# electric_car = ElectricCar("Tesla",90_000,"red", 100)
#
#
# electric_car.battery = 200
# print(electric_car.battery)
#
# print(electric_car.introduce())
#
#
#

"""Наследование"""
# class Transport:
#     def __init__(self, speed):
#         self.speed = speed
#     def __str__(self):
#         return f"Speed: {self.speed}"
#
# class Car(Transport):
#     def __init__(self, speed, fuel):
#         super().__init__(speed)
#         self.fuel = fuel
#     def __str__(self):
#         return f"Speed: {self.speed}  Fuel: {self.fuel}"
#
# transport = Transport(5)
# car = Car(5, 5)

# print(transport)
# print(car)

"""Полиформизм"""
# class Transport:
#     def __init__(self, speed):
#         self.speed = speed
#     def move(self):
#         return f"Transport speed: {self.speed} km/h"
#
# class Car(Transport):
#     def __init__(self, speed, fuel):
#         super().__init__(speed)
#         self.fuel = fuel
#     def move(self):
#         return f"Car speed: {self.speed} km/h, fuel: {self.fuel} AI"
#
# transport = Transport(5)
# car = Car(5, 95)
# print(transport.move())
# print(car.move())

"""Инкапсуляция"""
# class Transport:
#     def __init__(self, speed):
#         self.speed = speed
#     def move(self):
#         return f"Transport speed: {self.speed} km/h"
#
# class Car(Transport):
#     def __init__(self, speed, fuel):
#         super().__init__(speed)
#         self.__fuel = fuel
#     def move(self):
#         return f"Car speed: {self.speed} km/h, fuel: {self.fuel} AI"
#     @property
#     def fuel(self):
#         return self.__fuel
#     @fuel.setter
#     def fuel(self, fuel):
#         self.__fuel = fuel
#         return self.__fuel
#     def __str__(self):
#         return f"{self.speed} km/h, fuel: {self.fuel} AI"
#
#
# transport = Transport(5)
# car = Car(5, 95)
# print(transport.move())
# print(car.move())
#
# car.fuel = 92
# print(car)

"""Абстракция"""
# from abc import ABC,abstractmethod
#
# class Employee(ABC):
#     def __init__(self,name):
#         self.name=name
#     @abstractmethod
#     def calculate_month(self):
#         pass
#
# class FixedSalaryEmployee(Employee):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary = salary
#     def calculate_month(self):
#         return f"Name: {self.name}, Salary: {self.salary}"
#
# class HourlyEmployee(Employee):
#     def __init__(self,name, hours_worked, hourly_rate):
#         super().__init__(name)
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate
#     def calculate_month(self):
#         return f"Name: {self.name}, Hourly Rate: {self.hours_worked * self.hourly_rate}"
#
# class Freelancer(Employee):
#     def __init__(self,name,project_payment):
#         super().__init__(name)
#         self.project_payment = project_payment
#     def calculate_month(self):
#         return f"Name: {self.name}, Project Payment: {self.project_payment}"
#
# salary_employee = FixedSalaryEmployee("Dastan",100_000)
# hour_employee = HourlyEmployee("Ilim",1000, 200)
# freelancer_employee = Freelancer("Darika", 150_000)
#
# print(salary_employee.calculate_month())
# print(hour_employee.calculate_month())
# print(freelancer_employee.calculate_month())



class Bank:
    def __init__(self, name,age):
        self.name = name
        self.age = age

class Admin(Bank):
    def __init__(self,name,age, salary):
        super().__init__(name,age)
        self.salary = salary
    def __str__(self):
        return f'{self.name} {self.age} {self.salary}'

class Employee(Admin):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus
    def __str__(self):
        return f'{self.name} {self.age} {self.salary + self.bonus}'

admin = Admin('Dastan', 22, 100_000)
employee = Employee('Ilim', 18, 80_000, 5000)
print(admin)
print(employee)



"""
kiss
dry
solid
venv
create venv
python -m venv venv

activate
windows --> venv Scripts activate
mac linux --> source venv bin activate

pip install _____
pip freeze > requirements.txt
pip install -r requirements.txt

"""

