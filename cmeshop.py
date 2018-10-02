class Equipment:

    def __init__(self,name,damage,value):
        self.name = name
        self.damage = int(damage)
        self.value = value

class Player:

    def __init__(self,health, playername, playergender, playerpronoun, playergold):
        self.health = health
        self.playername = playername
        self.playergender = playergender
        self.playerpronoun = playerpronoun
        self.inventory = []
        self.gold = playergold
        self.location = 0
        self.equipment = None

    def equip(self):
        if len(self.inventory) > 0:
            print("                *----------------------------------------------*")
            print("                |                 Equipment                    |")
            print("                *----------------------------------------------*")
            for x in range(len(self.inventory)):
                print(f"                |               {[x]} {player.inventory[x].name}            {(9-(len(player.inventory[x].name))) * ' '}      |")
            print("                *----------------------------------------------*")
            equipmentvalue = int(input("                                     "))
            self.equipment = self.inventory[equipmentvalue]
        else:
            print("You don't have anything to equip")
    def forward(self):
        self.location += 1
        if rooms[self.location].monster in monsters:
            combat.combatflow(rooms[self.location].monster)
        elif rooms[self.location].shopkeeper == True:
            shopping.shopping()

    def back(self):
        if self.location != 0:
            self.location -= 1
            combat.combatflow(monsters[self.location])
        else:
            print("                          o--------------------o")
            print("                          | You can't go back! |")
            print("                          o--------------------o")
            print("                                               ")
            print("                                               ")
            print("                                               ")
            print("                                               ")
    def run(self):
        if self.location != 0:
            print("                             You run away!")
            self.location -= 1
        else:
            print("You can't go back!")
    def talk(self):
            print("                    You have a great conversation")
    def set0(self):
        self.location = 0
    def check_inventory(self):
        if len(player.inventory) == 0:
            print("|You have nothing in your inventory|")
        else:
            print("                  #------------------------------------#")
            print("                  |    You have the following items:   |")
            for item in self.inventory:
                print(f"                  |             {item.name}              {(9-len(item.name))* ' '}|")
            print("                  #------------------------------------#")
    def check_stats(self):
        if self.equipment == None:
            print("                         *---------------------*")
            print(f"                         |      Name: {self.playername} {(3-(len(self.playername))) * ' '}     |")
            print(f"                         |      Health: {self.health}      |")
            print(f"                         |       Gold: {self.gold}       |")
            print(f"                         |   Equipped: {self.equipment}    |")
            print("                         *---------------------*")
        else:
            print("                         *---------------------*")
            print(f"                         |      Name: {self.playername} {(3-(len(self.playername))) * ' '}     |")
            print(f"                         |      Health: {self.health}      |")
            print(f"                         |       Gold: {self.gold}       |")
            print(f"                         | Equipped: {self.equipment.name} |")
            print("                         *---------------------*")


class Monster:

    def __init__(self,name,adjective, health, damage, xp,inventory):
        self.health = int(health)
        self.name = name
        self.monstergender = "None"
        self.monsterpronoun = "None"
        self.inventory = inventory
        self.gold = 1
        self.xp = 1
        self.damage = 1
        self.location = 1
        self.adjective = adjective
        self.nearplayer = 0

class Room:
    def __init__(self, location, description, monster,shopkeeper):
        self.location = location
        self.description = description
        self.monster = monster
        self.shopkeeper = shopkeeper

    def combatstart(self,monster):
        combat.combatflow(monster=monsters[player.location])

    def roomshopping(self):
        if self.shopkeeper == True:
            shopping.shopping()

class Combat:
    def __init__(self, monster):
        self.player_alive = True
        self.monster = monster

    def attack(self):
        if player.equipment != None:
            print(f"You attack the {self.monster.name} for {1+player.equipment.damage} damage!")
            self.monster.health -= 1 + player.equipment.damage
        else:
            print("You attack the monster for 1 damage")
            self.monster.health -= 1

    def combatflow(self,monster):
        print("                                      ")
        print(f"                         #----------------{(len(self.monster.name) - len(self.monster.adjective))*'-'}--#")
        print(f"                         | A {self.monster.name} appears!|")
        print(f"                         | He looks {self.monster.adjective}. {(len(self.monster.name) - len(self.monster.adjective))*' '}|")
        print(f"                         #----------------{(len(self.monster.name) - len(self.monster.adjective))*'-'}--#")
        print("                                      ")
        while self.monster.health > 0:
            print("                              +--------+")
            print("                              | ATTACK |")
            print("                              |  TALK  |")
            print("                              |  FLEE  |")
            print("                              +--------+")
            playerinput = input("                                 ")
            if playerinput == "attack":
                self.attack()
            elif playerinput == "talk":
                player.talk()
            elif playerinput == "flee":
                player.run()
                player.location -=1
                break
            elif playerinput == "flee" and player.location == 0:
                print("You can't go back!")
        if self.monster.health <= 0:
            print("                                                       ")
            print("              !!!-----------------------------------!!!")
            print("               |              You win!               | ")
            print("               |      You get the following loot:    | ")
            print("              !!!-----------------------------------!!!")
            if (monsters[player.location].inventory) == None:
                print("               |  The monster didn't have anything.  | ")
                print("              !!!-----------------------------------!!!")
            else:
                player.inventory.append(monsters[player.location].inventory)
                for item in monsters[player.location].inventory:
                    print(f"                    |You got {monsters[player.location].inventory}|")
                    print("     --------------------------------------")
            if monsters[player.location].gold >= 0:
                player.gold = player.gold + monsters[player.location].gold
                print(f"               |        You got {monsters[player.location].gold} gold              |")
                print("              !!!-----------------------------------!!!")
            else:
                print("                 |       You didn't get any Gold         |       ")
                print("             !!!-------------------------------------!!!")
            rooms[player.location].monster = None
            print("                                            ")
            print("                                            ")
            print("                                            ")
            print("                                            ")
class Shopkeeper:
    def __init__(self):
        self.location = 4

    def shopping(self):
        print("%---------------------------------------------------------------------%")
        print("|             'Well? What do you want? I don't have all day.'         |")
        print("|A portly shopkeeper eyes you annoyedly as he takes drags from a pipe.|")
        print("%---------------------------------------------------------------------%")
        # Initial variable to track shopping status
        shopping = 'y'

        # List to track equipment purchases
        equipment_purchases = [0,0,0,0,0,0]

        # Equipment List
        equipment_list = weapons

        # While we are still shopping...
        while (shopping == "y" and player.gold > 0):

            # Show equipment selection prompt
            print("---------------------------------------------------------------------")
            print("(1) Longsword, (2) Steel Shield, (3) Longbow, (4) Spellbook, " +
                  " (5) 100ft of Rope, (6) Iron Rations")

            equipment_choice = input("Which would you like? ")

            # Get index of the equipment from the selected number
            choice_index = int(equipment_choice) - 1

            # Add equipment to the equipment list by finding the matching index and adding one to its value
            equipment_purchases[choice_index] += 1
            player.inventory.append(equipment_list[choice_index])
            player.gold -= 1
            print("------------------------------------------------------------------------")

            # Inform the customer of the equipment purchase
            print("Great! We'll have that " + equipment_list[choice_index].name + " right out for you.")

            # Provide exit option
            shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

        # Once the equipment list is complete
        print("------------------------------------------------------------------------")

        # Counts gold before display new equipment
        if player.gold == 0:
            print("You're broke? Get out you bum!")
        else:
            print("Come back if you need anything else.")

        print("------------------------------------------------------------------------")
        # Count instances of each piece of equipment
        print("You purchased: ")

        # Loop through the full equipment list
        for equip_index in range(len(equipment_list)):
            equipment_count = str(equipment_purchases[equip_index])
            equipment_name = equipment_list[equip_index].name

            # Gather the count of each pie in the pie list and print them alongside the pies
            print(equipment_count + " " + equipment_name)

        print("--------------------------------------------------------------------")

class Introduction:
    def __init__(self):
        self.firsttime = True
        self.playername = None
        self.playergender = None
        self.playerpronoun = None
        self.playercourage = None
        self.playerhealth = None
        self.playerwealth = None
        self.playergold = None
    def introinfo(self):
        print("                     *--------------------------------*")
        print("                     |  Tell me your name, traveler.  |")
        print("                     *--------------------------------*")
        self.playername = input("                                     ")
        print("                     *---------------------------------*")
        print(f"                     |  Are you a man or a woman, {self.playername}? {(2-(len(self.playername)))*' '}|")
        print("                     *---------------------------------*")
        self.playergender = input("                                     ")
        if self.playergender == "man":
            self.playerpronoun = "he"
        elif self.playergender == "woman":
            self.playerpronoun = "they"
        else:
            self.playerpronoun = "they"
        print("                 *------------------------------------------*")
        print(f"                 | Tell me {self.playername}, are a brave or cowardly {self.playergender}?{(3-(len(self.playergender)))*' '}|")
        print("                 *------------------------------------------*")
        self.playercourage =input("                                    ")
        if self.playercourage == "brave":
            self.playerhealth = 3
        elif self.playercourage == "cowardly":
            self.playerhealth = 5
        else:
            self.playerhealth = 7
        print("                      *------------------------------*")
        print("                      |  Do you love or hate money?  |")
        print("                      *------------------------------*")

        self.playerwealth = input("                                  ")
        if self.playerwealth == "hate":
            self.playergold = 1
        elif self.playerwealth == "love":
            self.playergold = 3
        else:
            self.playergold = 5

        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
        print("                                                        ")
introduction = Introduction()
introduction.introinfo()

# Initializing Classes
player = Player(introduction.playerhealth, introduction.playername, introduction.playergender, introduction.playerpronoun, introduction.playergold)

# Creating weapons
longsword = Equipment("Longsword",1,1)
longbow = Equipment("Longbow", 1, 1)
spellbook = Equipment("Spellbook", 2, 1)
weapons = [longsword,longbow,spellbook]

# Creating Monsters
goblin = Monster("goblin", "sickly", 1,1,1, None)
skeleton = Monster("skeleton", "bony", 1,1,1, None)
kobold = Monster("kobold", "curt", 1, 1,1, None)
evilthief = Monster("evil thief", "shadowy", 4,2,2,longsword)
monsters = [goblin, skeleton, kobold, evilthief]

# Creating Rooms
entrance = Room(0, "You see the entrance to a massive cave.", goblin,False)
firstroom = Room(1, "You enter a room ensconced in stone.", skeleton,False)
secondroom = Room(2, "You enter a dark room. A single torch burns in the corner.", kobold,False)
thirdroom = Room(3, "You enter test room 1.", evilthief,False)
fourthroom = Room(4, "You enter test room 2.", 0, True)
rooms = [entrance, firstroom, secondroom,thirdroom, fourthroom]

# Creating Combat
combat = Combat(monster=monsters[player.location])

# Creating Shopkeeping
shopping = Shopkeeper()

running = True
player.inventory.append(longsword)
player.inventory.append(longbow)

while running == True:
    print("                                                 ")
    print("                       *--------------------------*")
    print("                       |What would you like to do?|")
    print("                       |--------------------------|")
    print("                       |forward ---- Move forward.|")
    print("                       |back ---- Move backwards. |")
    print('                       |look ---- Look around.    |')
    print('                       |inv ---- Check inventory. |')
    print('                       |equip ---- Equip weapon.  |')
    print('                       |stats ---- Check stats.   |')
    print("                       *--------------------------*")
    print("                                                 ")
    playerinput = input("                                  ")
    if playerinput == "forward":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        player.forward()
    elif playerinput == "back":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        player.back()
    elif playerinput == "look":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                 *-----------------------------------------*")
        print(f"                 | {rooms[player.location].description} |")
        print("                 *-----------------------------------------*")
        print("                                   ")
    elif playerinput == "inv":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        player.check_inventory()
        print("                                   ")
    elif playerinput == "equip":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        player.equip()
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
        print("                                   ")
    elif playerinput == "stats":
        print("                                   ")
        print("                                   ")
        print("                                   ")
        player.check_stats()
        print("                                   ")

    else:
        print("Try another command")
        print("-----------------------------------")

#print("TESTING ABILITIES")
#print("---------------------------------------------------")
#print("---------------------------------------------------")
#print("MOVING")
#print("---------------------------------------------------")
#print(f"You are currently in room {player.location}")
#player.forward()
#print(f"You are currently in room {player.location}")
#player.back()
#print(f"You are currently in room {player.location}")
#player.back()
#print("MOVING TEST COMPLETE")
#print("---------------------------------------------------")
#print("INVENTORY/ EQUIPMENT")
#print("---------------------------------------------------")
#print(f"You pick up a {longsword.name}")
#player.inventory.append(longsword)
#player.equip()
#print(f"You have {player.equipment.name} equipped")
#print("INVENTORY AND EQUIPMENT TEST COMPLETE")
#print("---------------------------------------------------")