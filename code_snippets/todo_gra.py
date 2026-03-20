from games.dice import dice_game

wynik_handlarza, kostka_handlarza = dice_game.roll_dice()


#Opcja nr1
print("Rzuca hadnlarz")
print(kostka_handlarza)
print("Wynik rzutu handlarza  "  + str(wynik_handlarza))

print("Naciśnij enter żeby wykonać rzut")

# todo obsługa entera
# todo jak gracz wciśne enter to wykonuje się rzut

print("Rzuca gracz")
wynik_gracza, kostka_gracza = dice_game.roll_dice()
print(kostka_handlarza)
print("Twój wynik to  "  + str(wynik_handlarza))

#opcja nr2
wynik_handlarza2, kostka_handlarza2 = dice_game.roll_dice()
wynik_gracza2, kostka_handlarza2 = dice_game.roll_dice()

dice_game.print_two_dice(kostka_handlarza2, kostka_handlarza2)
pl1 = wynik_gracza2
pl2 = wynik_handlarza2

if(pl1>pl2):
    print("Gracz wygrywa!")
    #itd











