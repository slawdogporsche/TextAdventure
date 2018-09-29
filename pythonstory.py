import time

# Player Data
start_time = time.time()
playername = input("Player, what is your name? ")
playergender = input("Are you a boy or a girl? ")
playerpronoun = "blank"
if playergender == "boy":
    playerpronoun = "he"
elif playerpronoun =="girl":
    playerpronoun = "she"
else:
    playerpronoun = "they"

# Initial Variables
running = True
scenario = 1
inventory = []
health = 3
responseindex = 0
gold = 3

# Player Equipment Purchase
print("-----------------------------------------------------------------------")
print("You arrive in town on horseback, lured by rumors of a great treasure.")
print("An unequipped adventurer won't last long. You see the local shopkeeper.")
print("-----------------------------------------------------------------------")
print("'Well? What do you want? I don't have all day.'")
print("A portly shopkeeper eyes you annoyedly as he takes drags from a pipe.")

# Initial variable to track shopping status
shopping = 'y'

# List to track equipment purchases
equipment_purchases = [0,0,0,0,0,0]

# Equipment List
equipment_list = ["Longsword", "Steel Shield", "Longbow", "Spellbook", "100 ft of Rope", "Iron Rations"]

# While we are still shopping...
while (shopping == "y" and gold > 0):

    # Show equipment selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Longsword, (2) Steel Shield, (3) Longbow, (4) Spellbook, " +
          " (5) 100ft of Rope, (6) Iron Rations")

    equipment_choice = input("Which would you like? ")

    # Get index of the equipment from the selected number
    choice_index = int(equipment_choice) - 1

    # Add equipment to the equipment list by finding the matching index and adding one to its value
    equipment_purchases[choice_index] += 1
    inventory.append(equipment_list[choice_index])
    gold -= 1
    print("------------------------------------------------------------------------")

    # Inform the customer of the equipment purchase
    print("Great! We'll have that " + equipment_list[choice_index] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the equipment list is complete
print("------------------------------------------------------------------------")

# Counts gold before display new equipment
if gold == 0:
    print("You're broke? Get out you bum!")
else:
    print("Come back if you need anything else.")

print("------------------------------------------------------------------------")
# Count instances of each piece of equipment
print("You purchased: ")

# Loop through the full equipment list
for equip_index in range(len(equipment_list)):
    equipment_count = str(equipment_purchases[equip_index])
    equipment_name = str(equipment_list[equip_index])

    # Gather the count of each pie in the pie list and print them alongside the pies
    print(equipment_count + " " + equipment_name)

print("--------------------------------------------------------------------")

while (running == True and health > 0):
    if scenario == 0:
        print("You leave the scary dungeon. You wonder what life could have been.")
        print("                                                                  ")
        secondchance = input("You think about things a little. Maybe it's time to go back in? ")
        if secondchance == "yes":
            scenario += 1
        else:
            print("Fine! A freakin troll shows up and blasts your butt off")
            health -= 3
            print("You're dead and there's no troll treasure for you.")
            print("-------------------------------------------------------------")
    elif scenario == 1:
        print("You are at the entrance to a scary dungeon. What will you do?")
        player_input = input("Do you want to leave, or enter, or hit yourself? ")
        if player_input == "leave":
            scenario -= 1
        elif player_input == "enter":
            scenario += 1
            print("You enter the scary dungeon. What horrors await you?!")
            print("-----------------------------------------------------------------")
        elif player_input == "hit yourself":
            print("Stop hitting yourself!")
            health -= 1
            print(f"Your health is now {health}")
            print("                            ")
            if health == 0:
                print("You died. Nice going moron!")
                print("--------------------------------------------------------------------")
    elif scenario == 2:
        print("You see a big monster in front of you. It wants to eat you.")
        print("---------------------------------------------------------------------")
        print("                \\||/")
        print("                |  @___oo")
        print("      \\/\\  /\\   / (__,,,,|")
        print("     ) /^\\) ^\\/ _)")
        print("     )   /^\\/   _)")
        print("     )   _ /  / _)")
        print(" /\\  )/\\/ ||  | )_)")
        print("<  >      |(,,) )__)")
        print(" ||      /    \\)___)")
        print(" | \\____(      )___) )___")
        print("  \\______(_______;;; __;;;")
        print("--------------------------------------------------------------------")
        monsterresponse = input("Will you attack, run, or try to talk? ")
        if monsterresponse == "attack":
            scenario += 1
            print("-----------------------------------------------------------------")
        elif monsterresponse == "run":
            scenario -= 2
        elif (monsterresponse == "talk" and responseindex == 2):
            print("                                         ")
            print("Jesus you're persistent. He takes a bite out of your everything. ")
            health -= 1
            if health <= 0:
                print("You're troll food now. Now who's talking? Not you!")
        elif (monsterresponse == "talk" and responseindex == 2):
            print("                                         ")
            print("Jesus you're persistent. He takes a bite out of your everything. ")
            health -= 1
        elif (monsterresponse == "talk" and responseindex == 1):
            print("                                         ")
            print("What is wrong with you? He takes a bite out of your other leg. ")
            health -= 1
            responseindex += 1

        elif monsterresponse == "talk":
            print("                                          ")
            print("I don't think he's the talking type. He bites a chunk out of your leg. ")
            health -= 1
            responseindex = 1
            print(f"Your health is now {health}")
    elif (scenario == 3 and ("Longsword" in inventory)):
        print("You stab the monster with your mighty sword! It dies! Huzzah! ")
        print("                                                             ")
        print("You get a golden amulet.")
        inventory.append("golden amulet")
        print("                                              ")
        print(f"Your inventory currently contains {inventory}")
        print("                                              ")
        putitemdown = input("Would you like to put the amulet down?")
        if putitemdown == "yes":
            inventory.remove("golden amulet")
            print(f"Your inventory currently contains {inventory}")
        else:
            print(f"Your inventory currently contains {inventory}")
        scenario += 1
    elif (scenario == 3 and ("Longbow" in inventory)):
        print("You shoot the monster with your mighty longbow! It dies! Huzzah! ")
        print("                                                             ")
        print("You get a golden amulet.")
        inventory.append("golden amulet")
        print("                                              ")
        print(f"Your inventory currently contains {inventory}")
        print("                                              ")
        putitemdown = input("Would you like to put the amulet down? ")
        if putitemdown == "yes":
            inventory.remove("golden amulet")
            print(f"Your inventory currently contains {inventory}")
        else:
            print(f"Your inventory currently contains {inventory}")
        scenario += 1
    elif (scenario == 3 and ("Spellbook" in inventory)):
        print("You blast the monster with a mighty fireball! It dies! Huzzah! ")
        print("                                                             ")
        print("You get a golden amulet.")
        inventory.append("golden amulet")
        print("                                              ")
        print(f"Your inventory currently contains {inventory}")
        print("                                              ")
        putitemdown = input("Would you like to put the amulet down? ")
        if putitemdown == "yes":
            inventory.remove("golden amulet")
            print(f"Your inventory currently contains {inventory}")
        else:
            print(f"Your inventory currently contains {inventory}")
        scenario += 1
    elif (scenario == 3 and (["Longsword", "Longbow", "Spellbook"] not in inventory)):
        print("You try and attack with your bare fists. It goes about as well as you'd expect")
        print("The beast blasts you with a huge flame.")
        health -= 2
        print(f"You have {health} health")
        scenario = 2
    elif scenario == 4:
        print("                                  ")
        print("You are presented with two doors:")
        print("The door on the left is large, wooden, and foreboding. Bet there's a bat.")
        print("The door on the right is small and encircled with stone. It whistles with opportunity.")
        door_choice = input("Which door do you choose? Right or left? ")
        print("----------------------------------------------------------------")
        if (door_choice == "left" and "golden amulet" in inventory):
            print("You hear a loud whoosh as a burst of flame slams into you!")
            print("The amulet crumbles to dust, but you are unharmed!")
            print("--------------------------------------------------------------------------")
            scenario += 1
        elif(door_choice == "left" and ("golden amulet" not in inventory) and health <= 2):
            print("You get schwacked by a huge gust of flame. Roasted bro! ")
            print("You died.")
            break
        else:
            print("You enter the right room and come upon a mighty genie")
            print("                          .")
            print("       .:::.....:::::::..  :.")
            print("    .::::::::::::::::::::::.::.")
            print("   :       `::::::::::::::::::::.")
            print("               `::::::::::::::::::.")
            print("                       `::::::::::::")
            print("                         `::::::::::")
            print("                           `:::::::")
            print("           %%,   .::::.      `:::'      .::::.        ,%%%%")
            print("           `%%%, :::::::.    oOOOo    .:::::::.     ,%%;%%%")
            print("            `%%%,::%%%%::%%%%%%%%%%%%%::%%%%%::%   %%%;%%%")
            print("             `%%,%%%%%%%:%%%%%%%%%%%%%%%%%%%%:'%%,%%%;%%%")
            print("              %%,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,%%;%%%;")
            print("              %%,%;a@@@a;%%%%%%%%%;a@@@@@@a;%%%%%%%%%;%%%")
            print("        .oOOOo%,%;@@@@@@@a;%%%%%%;@@@@@@@@@a;%%%%%%,%%;%%")
            print("        OOO' .,%;a@@@@@@@@a;%%%%;@@@@@@@@@@@;%%%%%%%%,%;%,")
            print("        `OO.%%%%;@@@@@@@@@@;%%%;@@@@@@@@@@@@;%;%%%%%%%,%%%")
            print("          ;%%%%;%;@@@@@@@@@;%%%;@@@@@@@@@@@;;%%%%%%%%%,%%%")
            print("          `%%%%%%;;@@@@@@@@;%%%;@@@@@@@@@;%%%%%%%%%%%,%%%'")
            print("           `%%%%%%%;;@@' .;%%%%%, `@@@@;%%%%%%%;%%%%,%%%'")
            print("            `%;%;%%%%%%%%`%%%%%%%%%%%%%%%%;%;%;%%%%%,""")
            print("            :%%%;,%;%%`%%%%%%%%%%%%%%%%%%%%;;%%%::%%;")
            print("          ::%%%%;O;%%`%%%%%%%%%%%%%%%%%%%%;O;%%%%::%;")
            print("        ::%%%%%%;OO;%`%%%%%%%%%%%'%%%%%%%;OO;;%%%%::%")
            print("       ::%%%%%%;OOOOOO`%%%%%%%%'%%%%;OOOOOOOO;%%%%%::%")
            print("     ::%%%%%%%;OOOOOOOOOO`%%%%'OOOOOOOOOOOOOOO;%%%%%::.")
            print("   ::%%%%%%%%;                                ;%%%%%%::.")
            print("  ::%%%%%%%%;           ,;;;;;;;;;,;;;;;;;;;, ,;%%%%%%::.")
            print(" ::%%%%%%%;           .;;;;;;;;;;,;;;;;;;;;;;oO;%%%%%%%::")
            print("::%%%%%;OOo,.         ;;;;;;;;;;;;;;;;;;ooOOOOOO;%%%%%%::")
            print("::%%%%%;OOOOOOoOOOOOOOOoOOOOOOOOoOOOOOOOOOOOOOO;%%%%%%%::")
            print("::%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%::")
            print(" ::%%%%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%%%%::'")
            print("  `::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::'")
            print("    `:::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%::::'")
            print("      `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::::'")
            print("         `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%::::::'")
            print("            `:::::::::::::::::::::::::::::::'")
            print("               `:::::::::::::::::::::::::'")
            print("                  `::::::::::::::::::'")
            print("                     `:::::::::::'")
            print("                       `:::::::'")
            print("                       .::::'")
            print("                      .:::'")
            print("                     :::'")
            print("                    ::'   .::::.")
            print("                    ::.   ::  `::")
            print("                     ::.   `  .::")
            print("                      `::::::::'")
            print("---------------------------------------------------------------------")
            genieinput = input("What will you do? You can attack, talk, or flee. ")
            print("--------------------------------------------------------------------------")
            if (genieinput =="attack" and ("golden amulet" not in inventory)):
                print("------------------------------------------------------------------------")
                print("Attacking an immortal diety probably isn't a great idea.")
                print("With a snap of his fingers, the genie turns you into a duck.")
                print("To be clear, the genie didn't kill you.")
                print("But you probably won't last long in a dungeon.")
                print("-------------------------------------------------------------------------")
                break
            elif (genieinput =="attack" and ("golden amulet" in inventory)):
                print("The genie attempts to cast a spell on you, but your amulet protects you!")
                print("The amulet crumbles to dust")
                inventory.remove("golden amulet")
                print("You run from the room before he can whack you again")
                print("-------------------------------------------------------------------------")
            elif genieinput == "talk":
                print("The genie eyes you curiously. What pretension, for a mortal to talk to a god!")
                print("The genie likes your spunk, and awards you with a powerful magic item.")
                print("The fabled 'Brooks Brothers Polka Dot Shirt")
                inventory.append("Brooks Brothers Polka Dot Shirt")
                print(inventory)
                print("-------------------------------------------------------------------------")
                scenario += 1

    elif scenario == 5:
        print("You finally come upon the treasure. Boy, that wasn't very well guarded...")
        print("-------------------------------------------------------------------------")
        print("Many years later, you die happily.")
        print("-------------------------------------------------------------------------")
        break
    else:
        print("How did you get here?")
        break

elapsed_time = time.time() - start_time
playerfinalhealth = health
if playerfinalhealth == 3:
    playerfinalhealth = "excellent"
elif playerfinalhealth == 2:
    playerfinalhealth = "good"
elif playerfinalhealth == 1:
    playerfinalhealth = "poor"
else:
    playerfinalhealth = "fucked up"

print(f"Here lies {playername}, buried with the {inventory} {playerpronoun} so cherished.")
print(f"Last known to be in {playerfinalhealth} health, on a journey of {elapsed_time} seconds")
## genie
## add functions
## add health bar

