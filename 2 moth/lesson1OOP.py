# shops = []
# class Product:
#     def __init__(self, name, price, date, sale=0):
#         self.name = name
#         self.price = price
#         self.sale = sale
#         self.date = date
#         self.acctual_price = (self.price * self.sale) / 100 if self.sale else self.price
#
#     def __str__(self):
#         return f"""
# name: {self.name}
# price: {self.price}
# sale: {self.sale}
# acctual_price: {self.acctual_price}
# date: {self.date}
# """
#
#     def add(self):
#         shops.append(dict(name=self.name, price=self.price, sale=self.sale, acctual_price=self.acctual_price, date=self.date))
#
# sugar = Product("sugar", 20, "12.02.2026", )
# sugar2 = Product("salt", 20, "12.02.2026", )
#
# sugar.add()
# sugar2.add()
#
# print(shops)
#

# import random
# class Robot:
#     def __init__(self, name, power, healts):
#         self.name = name
#         self.power = power
#         self.healts = healts
#     def __str__(self):
#         return f'{self.name}, {self.power}, {self.healts}'
#     def attack(self, other_robot):
#         damage = random.randint(1, 100)
#         other_robot.healts -= damage
#         print(f'{self.name} attacked {damage} damage')
#         print(f'{other_robot.name} healts {other_robot.healts}')
#
#
# robot = Robot("Optimus", 100, 100)
# robot2 = Robot("Kibertron", 100, 100)
# robot.attack(robot2)
# robot2.attack(robot)


class Hero:
    def __init__(self, name, healts, damage):
       ...

class Archer(Hero):
    def __init__(self, name, healts, damage, arrow):
        self.name = name
        self.healts = healts + 999
        self.damage = damage
        self.arrow = arrow

class Warrior(Hero):
    def __init__(self, name, healts, damage,x):
        super().__init__(name, healts, damage)
        self.x = x


arr = Archer("hhj",777,"jjjkj",99)
print(arr.healts)


