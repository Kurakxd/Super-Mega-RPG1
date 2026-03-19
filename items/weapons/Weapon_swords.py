from items.weapons.Weapon import Weapon

weapons = {
    "sword": Weapon("Miecz", 10, "🗡️"),
    "dagger": Weapon("Sztylet", 15, "🗡️"),
    "axe": Weapon("Topór", 10, "🪓"),
    "spear": Weapon("Włócznia", 8, "🔱")
}

def show_weapons(weapons_dict):
    print("\n=== ⚔️ DOSTĘPNE BRONIE ===\n")

    for key, weapon in weapons_dict.items():
        print(f"[{key:<6}]  {weapon}")

    print("\n=========================\n")