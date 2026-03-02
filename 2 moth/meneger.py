class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"name: {self.name}\nsalary: {self.salary}\n"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def __str__(self):
        return f"nama: {self.name}\nbonus: {self.bonus}\nsalary: {self.salary + self.bonus}"


employee = Employee("Dastan", 10000)
manager = Manager("Ilim", 10000, 100)

persons = [employee,manager]
for person in persons:
    print(person)


