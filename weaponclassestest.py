class Equipment:

    def __init__(self,name,damage,value):
        self.name = name
        self.damage = damage
        self.value = value

weapons = [Equipment("Longsword", 1, 1), Equipment("Longbow", 1, 1), Equipment("Spellbook", 1, 1)]
weaponlist = []
for weapon in weapons:
    weaponlist.append(weapon)

print(weaponlist[0].damage)

if len(weaponlist) > 0:
    for x in range(len(weaponlist)):
        print(f"{[x]} {weaponlist[x].name}")
        equipmentvalue = int(input("Which would you like to equip? "))
        if equipmentvalue == x:


