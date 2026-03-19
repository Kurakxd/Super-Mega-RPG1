from items.weapons.Weapon_swords import weapons, show_weapons

show_weapons(weapons)

for key, weapon in weapons.items():
    print("Test obrażeń broni")
    print("MAX damage dla: " + weapon.name + " : " + str(weapon.damage) +" | Zadane Obrażenia " + str(weapon.attack()) )
