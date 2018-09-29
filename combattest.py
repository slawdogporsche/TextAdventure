class Equipment:

    def __init__(self,name,damage,value):
        self.name = name
        self.damage = int(damage)
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
        self.equipment = 0

    def attack(self):
            if self.equipment != 0:
                print(f"You attack the monster for {1+self.equipment.damage} damage")
                monsters[self.location].health -= 1 + self.equipment.damage
            else:
                print("You attack the monster for 1 damage")

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
    def forward(self):
        self.location += 1
        print(rooms[self.location].description)
        rooms[self.location].monster
        combat.combatflow(monsters[self.location])

    def back(self):
        if self.location != 0:
            self.location -= 1
            print(rooms[self.location].description)
            combat.combatflow(monsters[self.location])
        else:
            print("You can't go back!")
    def run(self):
            print("You run away!")
            self.location -= 1
    def talk(self):
            print("You have a great conversation")
    def set0(self):
        self.location = 0

class Monster:

    def __init__(self,name,adjective, health, damage, xp):
        self.health = int(health)
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

class Room:
    def __init__(self, location, description, monster):
        self.location = location
        self.description = description
        self.monster = monster

    def combatstart(self,monster):
        combat.combatflow(monster=monsters[player.location])
    def roomaction(self):
        if player.location == self.location:
            print("what would you like to do?")

class Combat:
    def __init__(self, monster):
        self.player_alive = True
        self.monster = monster

    def combatflow(self,monster):
        print("Fight fight fight!")
        print(f"You approach the {monster.name}. He looks {monster.adjective}")
        while monster.health >= 0:
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
                player.location -=1

            print("--------------------------------------")
            print("You win!")
            print("You get the following loot!")
            print("--------------------------------------")
            if len(monster.inventory) == 0:
                print("The monster didn't have anything")
            else:
                player.inventory.append(monster.inventory)
                print(f"You got {monster.inventory}")
            print("--------------------------------------")
            if monster.gold >= 0:
                player.gold = player.gold + monster.gold
                print(f"You got {monster.gold} gold")
            else:
                print("You didn't get any gold")
                print("-------------------------------------")
            break

# Initializing Classes
player = Player()

# Creating weapons
longsword = Equipment("Longsword",1,1)
longbow = Equipment("Longbow", 1, 1)
spellbook = Equipment("Spellbook", 2, 1)

# Creating Monsters
goblin = Monster("goblin", "sickly", 1,1,1)
skeleton = Monster("skeleton", "bony", 1,1,1)
kobold = Monster("kobold", "curt", 1, 1,1)
evilthief = Monster("evil thief", "shadowy", 4,2,2)
monsters = [goblin, skeleton, kobold, evilthief]

# Creating Rooms
entrance = Room(0, "You see the entrance to a massive cave", goblin)
firstroom = Room(1, "You enter a room ensconced in stone", skeleton)
secondroom = Room(2, "You enter a dark room. A single torch burns in the corner", kobold)
rooms = [entrance, firstroom, secondroom]

# Creating Combat
combat = Combat(monster=monsters[player.location])

print("TESTING ABILITIES")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("MOVING")
print("---------------------------------------------------")
print(f"You are currently in room {player.location}")
player.forward()
print(f"You are currently in room {player.location}")
player.back()
print(f"You are currently in room {player.location}")
player.back()
print("MOVING TEST COMPLETE")
print("---------------------------------------------------")
print("INVENTORY/ EQUIPMENT")
print("---------------------------------------------------")
print(f"You pick up a {longsword.name}")
player.inventory.append(longsword)
player.equip()
print(f"You have {player.equipment.name} equipped")
print("INVENTORY AND EQUIPMENT TEST COMPLETE")
print("---------------------------------------------------")