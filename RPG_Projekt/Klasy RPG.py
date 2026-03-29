import random
def klasa(wybor_klasa):
    if wybor_klasa == 1:
        return {"klasa": "Wojownik", "Życie gracza": 120, "atak": random.randint(10, 15)}
    elif wybor_klasa == 2:
        return {"klasa": "Mag", "Życie gracza": 65, "atak": random.randint(20, 30)}
    elif wybor_klasa == 3:
        return {"klasa": "Łotr", "Życie gracza": 80, "atak": random.randint(15, 20)}