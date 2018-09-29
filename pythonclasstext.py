class Equipment:

    def __init__(self,name,damage,value):
        self.damage = 1
        self.value = 1
        self.name = name

class Player:

    def __init__(self):
        self.health = 3
        self.playername = "None"
        self.playergender = "None"
        self.playerpronoun = "None"
        self.inventory = []
        self.gold = 3
        self.location = 0
        self.equipment = "None"

    def attack(self):
        if player.location == monster.location:
            print("You attack the monster")
            monster.health -= 1
    def equip(self):
        if self.inventory:
            print("Pick which of your weapons you'd like to equip")
            print(self.inventory)
            self.equipment = input("Which would you like to equip?")
    def move(self):
        self.location += 1

class Monster:

    def __init__(self):
        self.health = 3
        self.monstername = "None"
        self.monstergender = "None"
        self.monsterpronoun = "None"
        self.inventory = []
        self.gold = 1
        self.location = 1

    def death(self):
        if self.health == 0:
            print("The monster died.")

player = Player()
monster = Monster()
equipment = Equipment()
Longsword = Equipment("Longsword", 1, 1)
Longbow = Equipment("Longbow", 1, 1)


print("You pick up a Longsword")
player.inventory.append(Longsword)
print(player.inventory)
print(equipment.name)
