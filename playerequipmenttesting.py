class Equipment:

    def __init__(self,name):
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
        if 1 == 1:
            print("Pick which of your weapons you'd like to equip")
            print("----------------------------------------------")
            for x in range(2):
                print(f"{[x]} {player.inventory[x].name}")
            equipmentvalue = int(input("Which would you like to equip? "))
            if equipmentvalue == 0:
                self.equipment = longsword
    def move(self):
        self.location += 1

player = Player()
longsword = Equipment("Longsword")
longbow = Equipment("Longbow")
spellbook = Equipment("Spellbook")

#print("Some initial commands for showing that functions work")
    #print("This shows the player's inventory initially.")
    #print (player.inventory)
    #print("-------------------------------------------")
    #print("This shows the addition of an item to the inventory.")
    #print("You stumble upon a Longsword!")
    #player.inventory.append(longsword)
    #print("You now have the following items:")
    #print(player.inventory[0].name)
    #print("-------------------------------------------")
    #print("This shows the addition of a longbow and displays the total inventory.")
    #print("You stumble upon a Longbow!")
    #player.inventory.append(longbow)
    #print("You now have the following items:")
    #for x in range(2):
    #    print(player.inventory[x].name)
    #print(player.inventory[0].name)
    #print(player.inventory[1].name)
    #print("-------------------------------------------------")
    #player.equip()
    #print(player.equipment.damage)


