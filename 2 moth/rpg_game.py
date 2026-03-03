from abc import ABC, abstractmethod
import random

class Game(ABC):
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    @abstractmethod
    def attack(self, enemy):
        pass

    def __str__(self):
        return f"{self.name} health: {self.health}"

    def is_alive(self):
        return self.health > 0

    def team_fight(self, heroes):

        while self.is_alive() and any(hero.is_alive() for hero in heroes):

            print("\n=== NEW ROUND ===")

            for hero in heroes:
                if hero.is_alive():
                    if isinstance(hero, Healer):
                        hero.heal_ally(heroes)
                    else:
                        hero.attack(self)
                        print(f"{hero.name} attacks {self.name}")
                        print(f"{self.name} health: {self.health}")

            if not self.is_alive():
                break

            alive_heroes = [hero for hero in heroes if hero.is_alive()]
            target = random.choice(alive_heroes)

            self.attack(target)
            print(f"{self.name} attacks {target.name}")
            print(f"{target.name} health: {target.health}")

        print("Game Over")

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Boss(Game):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
    def __str__(self):
        return f"{self.name} health: {self.health}"

    def attack(self, enemy):
        damage = random.randint(1, 100)
        enemy.receive_damage(damage)

class Warrior(Game):
    def __init__(self, name, health, damage, critical_damage):
        super().__init__(name, health, damage)
        self.critical_damage = critical_damage
    def __str__(self):
        return f"{self.name} health: {self.health}"

    def attack(self, enemy):
        damage = random.randint(1, 50)
        if random.randint(1, 100) <= self.critical_damage:
            damage *= 2
            print("Critical damage")

        enemy.receive_damage(damage)

class Archer(Game):
    def __init__(self, name, health, damage, critical_arrow):
        super().__init__(name, health, damage)
        self.critical_arrow = critical_arrow
    def __str__(self):
        return f"{self.name} health: {self.health}"

    def attack(self, enemy):
        damage = random.randint(1, 60)
        if random.randint(1, 100) <= self.critical_arrow:
            damage *= 2
            print("Critical arrow")

        enemy.receive_damage(damage)

class Healer(Game):
    def __init__(self, name, health, damage, heal):
        super().__init__(name, health, damage)
        self.heal = heal
    def __str__(self):
        return f"{self.name} health: {self.health}"

    def attack(self, healer):
        pass

    def heal_ally(self, heroes):
        alive = [h for h in heroes if h.is_alive()]
        if alive and random.randint(1, 100) <= 30:
            target = min(alive, key=lambda h: h.health)
            target.health += self.heal
            print(f"{self.name} heals {target.name} for {self.heal}")

boss = Boss("Boss", 1000, 0)
warrior = Warrior("Warrior", 200, 0, 30)
archer = Archer("Archer", 200, 0, 30)
healer = Healer("Healer", 200, 0, 30)

heroes = [warrior, archer, healer]
boss.team_fight(heroes)

for i in heroes:
    print(i)

