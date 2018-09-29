class Equipment:

    def __init__(self,name,damage,value):
        self.name = name
        self.damage = damage
        self.value = value

class Player:

    def __init__(self):
        self.health = 3
        self.playername = "None"
        self.playergender = "None"
        self.playerpronoun = "None"
        self.inventory = []
        self.gold = 3
        self.location = 0
        self.equipment = "none"

    def attack(self):
        if player.location == monster.location:
            print("You attack the monster")
            monster.health -= 1 + self.equipment.damage
    def equip(self):
        if len(self.inventory) > 0:
            print("Pick which of your weapons you'd like to equip")
            print("----------------------------------------------")
            for x in range(len(self.inventory)):
                print(f"{[x]} {player.inventory[x].name}")
            equipmentvalue = int(input("Which would you like to equip? "))
            if equipmentvalue == x:
                self.equipment = self.inventory[x]
        else:
            print("You don't have anything to equip")
    def move(self):
        self.location += 1
    def run(self):
        if player.location == monster.location:
            print("You run away!")
            self.location -= 1
    def talk(self):
        if player.location == monster.location:
            print("You have a great conversation")

class Monster:

    def __init__(self,name,adjective, health):
        self.health = 3
        self.name = name
        self.monstergender = "None"
        self.monsterpronoun = "None"
        self.inventory = []
        self.gold = 1
        self.location = 1
        self.adjective = adjective
        self.nearplayer = 0

# Initializing Classes
player = Player()
monster = Monster("monster", "adjective", 1)

# Creating Weapons
weapons = [Equipment("Longsword", 1, 1), Equipment("Longbow", 1, 1), Equipment("Spellbook", 1, 1)]
generated_weapons =[]
for weapon in weapons:
    generated_weapons.append(weapon)

print("List of all generated weapon items.")
print(generated_weapons)
print("----------------------------------------------------")
print("Name of first weapon in list of weapons.")
print(generated_weapons[0].name)

print("Picking up and equipping items")
player.inventory.append(generated_weapons[0])
print(player.inventory[0].name)
player.equip()
print(f"You have the {player.equipment.name} equipped")

## PICKING UP AND EQUIPPING WEAPONS
#print(f"You pick up a {Longsword.name}")
#player.inventory.append(Longsword)
#player.equip()
#print(f"You have {player.equipment.name} equipped")