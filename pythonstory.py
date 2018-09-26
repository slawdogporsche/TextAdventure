running = True
scenario = 1
inventory = []
health = 3
responseindex = 0
while (running == True and health > 0):
    if scenario == 0:
        print("You leave the scary dungeon. You wonder what life could have been.")
        print("                                                                  ")
        secondchance = input("You think about things a little. Maybe it's time to go back in?")
        if secondchance == "yes":
            scenario += 1
        else:
            print("Fine! A freakin troll blasts your butt off")
            health -= 3
            print("You're dead and there's no troll treasure for you.")
    elif scenario == 1:
        print("You are at the entrance to a scary dungeon. What will you do?")
        player_input = input("Do you want to leave, or enter, or hit yourself? ")
        if player_input == "leave":
            scenario -= 1
        elif player_input == "enter":
            scenario += 1
            print("You enter the scary dungeon. What horrors await you?!")
            print("                                                     ")
        elif player_input == "hit yourself":
            print("Stop hitting yourself!")
            health -= 1
            print(f"Your health is now {health}")
            print("                            ")
            if health == 0:
                print("You died. Nice going moron!")
    elif scenario == 2:
        print("You see a big monster in front of you. It wants to eat you.")
        monsterresponse = input("Will you attack, run, or try to talk? ")
        if monsterresponse == "attack":
            scenario += 1
            print("                                         ")
            print("You attack the monster. You're so brave! ")
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
    elif scenario == 3:
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
            print(inventory)
        scenario += 1
    elif scenario == 4:
        print("                                  ")
        print("You are presented with two doors. ")
        print("The door on the left is large, wooden, and foreboding. ")
        print("The door on the right is small and encircled with stone.")
        door_choice = input("Which door do you choose? Right or left? ")
        print("                                                       ")
        if (door_choice == "left" and "golden amulet" in inventory):
            print("You open the door and a great burst of flame hits you in the chest")
            print("The amulet crumbles to rust, but you are unharmed!")
            break
        elif(door_choice == "left" and ("golden amulet" not in inventory) and health <= 2):
            print("You get schwacked by a huge gust of flame. Roasted bro! ")
            print("You died.")
            break
        else:
            print("You enter the right room and you get hella skrilla")
            break
    else:
        print("How did you get here?")
        break



