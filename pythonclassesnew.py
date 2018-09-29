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

    def __init__(self,name,adjective, health, damage, xp):
        self.health = 3
        self.name = name
        self.monstergender = "None"
        self.monsterpronoun = "None"
        self.inventory = []
        self.gold = 1
        self.xp = 1
        self.damage = 1
        self.location = 1
        self.adjective = adjective
        self.nearplayer = 0

# Initializing Classes
player = Player()
monster = Monster("monster", "adjective", 1,1,1)

# Creating Weapons
weapons = [Equipment("Longsword", 1, 1), Equipment("Longbow", 1, 1), Equipment("Spellbook", 1, 1)]
generated_weapons =[]
for weapon in weapons:
    generated_weapons.append(weapon)

Longsword = Equipment("Longsword",1,1)
Longbow = Equipment("Longbow", 1, 1)
Spellbook = Equipment("Spellbook", 2, 1)

# Creating Monsters
goblin = Monster("goblin", "sickly", 1,1,1)
skeleton = Monster("skeleton", "bony", 1,1,1)
kobold = Monster("kobold", "curt", 1, 1,1)
evilthief = Monster("evil thief", "shadowy", 4,2,2)

# MOVEMENT
print(f"Current player location is {player.location}")
player.move()
print(f"Current player location is {player.location}")

# PICKING UP AND EQUIPPING WEAPONS
print(f"You pick up a {Longsword.name}")
player.inventory.append(Longsword)
player.equip()
print(f"You have {player.equipment.name} equipped")

# COMBAT
if player.location == monster.location:
    goblin.nearplayer +=1
    print("Fight fight fight!")
    print(f"You approach the {goblin.name}. He looks {goblin.adjective}")
    while (goblin.nearplayer == 1 and goblin.health >= 0):
        print("You have the following options")
        print("------------------------------------------------------")
        print("ATTACK")
        print("TALK")
        print("RUN")
        print("------------------------------------------------------")
        playerinput = input("What will you do?")
        if playerinput == "attack":
            player.attack()
        elif playerinput == "talk":
            player.talk()
        elif playerinput == "run":
            player.run()
            Goblin.nearplayer -=1
        if goblin.health >= 0:
            print("--------------------------------------")
            print("You win!")
            print("You get the following loot!")
            print("--------------------------------------")
            player.inventory.append(monster.inventory)
            player.gold = player.gold + goblin.gold
            print(f"You got {goblin.inventory}")
            print(f"You get {goblin.gold} gold")

            print("-------------------------------------")
            break





