class Weapon:
    def __init__(self, name, damage, emoji):
        # Konstruktor - wywoływany przy tworzeniu obiektu
        # np. Weapon("Miecz", 10, 0.2)
        self.name = name  # nazwa broni, np. "Miecz"
        self.damage = damage  # bazowe obrażenia, np. 10
        self.emoji = emoji  # ikonka broni (domyślnie ⚔️)


    # oblicza damage broni
    def attack(self):
        import random
        min_damage = self.damage // 2  # lepiej niż int(self.damage/2)
        total_damage = random.randint(min_damage, self.damage)
        return total_damage

    #metoda do printu broni
    def __str__(self):
        return f"{self.emoji} {self.name} | DMG: {self.damage}"