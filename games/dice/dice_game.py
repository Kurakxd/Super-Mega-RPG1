# importujemy moduł random, żeby losować liczby
import random

# importujemy nasze ASCII kostki z pliku dice_art.py
from games.dice.dice_art import DICE_GRAPHICS


# definiujemy funkcję, która będzie "rzucać kostką"
def roll_dice():
    # losujemy liczbę od 1 do 6 (symulacja rzutu kostką)
    value = random.randint(1, 6)

    # wybieramy odpowiednią grafikę ASCII z listy (index = value - 1) bo indeks 0 to 1 itd aż do indeksu 5, który oznacza liczbę 6
    art = DICE_GRAPHICS[value - 1]

    # zwracamy dwie rzeczy: wartość kostki i jej grafikę
    return value, art


# funkcja do wyświetlania dwóch kostek obok siebie
def print_two_dice(art1, art2):
    # dzielimy tekst na linie
    lines1 = art1.split("\n")
    lines2 = art2.split("\n")

    # łączymy linie parami i drukujemy obok siebie
    for l1, l2 in zip(lines1, lines2):
        print(l1 + "   " + l2)


def print_result(value_dice_1, value_dice_2):
    print(f"\n🎲 Wynik: Handlarz: {value_dice_1} | Gracz: {value_dice_2}"

# todo do naprawienia:
    # if (value_dice_1 > value_dice_2):
    #     print("Handlarz wygrywa!")
    # elif value_dice_1 == value_dice_2:
    #     print("Remis!")
    # else:
    #     print("Gracz wygrywa!")
)
