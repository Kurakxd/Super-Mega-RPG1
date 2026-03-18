import random

print("----SUPER ULTRA RPG----")
print("-----------------------")
print("--STWÓRZ SWOJĄ POSTAĆ--")
print("-----------------------")
print("1.---STWÓRZ BOHATERA---")
print("2.---STWÓRZ BOHATERA---")
print("3.---STWÓRZ BOHATERA---")

print("-----------------------")
stworz_bohatera = int(input("Wybierz zapis na którym chcesz grać: "))
print("-----------------------")

nazwa = input("Nazwij swojego bohatera: ")
print("-----------------------")
print("Witaj w świecie magii ", nazwa)
print("-----------------------")

CIOS_KRYTYCZNY = 0
bonus_atak = 0
zycie_gracza = 10000
zycie_wroga = 150
zycie_wroga1 = 300
srebrniki = 0
zlote_monety = 0

przedmioty = []
# ("-----------------------")
miecz_ogra = 0
if miecz_ogra == 0:
    miecz_ogra = False
else:
    miecz_ogra = True
# ("-----------------------")
smoczy_sztylet = 0
if smoczy_sztylet == 0:
    smoczy_sztylet = False
else:
    smoczy_sztylet = True
# ("-----------------------")
trolii_sztylet = 0
if trolii_sztylet == 0:
    trolii_sztylet = False
else:
    trolii_sztylet = True
# ("-----------------------")
wilcza_wlocznia = 0
if wilcza_wlocznia == 0:
    wilcza_wlocznia = False
else:
    wilcza_wlocznia = True

while True:

    print("1. Atak")
    print("Twój bonus do ataku:", bonus_atak)
    print("-------------")
    print("2. Leczenie")
    print("Twoje HP:", zycie_gracza, "/100")
    print("-------------")
    print("3. Dane gracza")
    print("-------------")
    print("4. Ekwipunek")
    print("-------------")
    print("5. Sklep")
    print("-------------")
    print("6. Ucieczka")
    print("-------------")

    wybór = int(input("Proszę wpisać cyfrę odpowiadającej danej opcji: "))

    if wybór == 1:
        print("-------------")
        print("1. Zaatakuj Ogra Marcina")
        print("2. Zatakuj Smoka Andrzeja")
        print("!! Uwaga Smok Andrzej jest mocniejszym przeciwnikiem od Ogra Marcina !!")
        print("-------------")

        wybór1 = int(input("Kogo chcesz zaatakować?: "))

        if wybór1 == 1:

            if zycie_wroga <= 0:
                print("----------------------------------")
                print("Ogr Marcin został już pokonany.")
                print("----------------------------------")
            else:
                CIOS_KRYTYCZNY = random.randint(1, 5)
                if CIOS_KRYTYCZNY == 2:
                    CIOS_KRYTYCZNY += 5
                else:
                    CIOS_KRYTYCZNY = 0
                obrazenia = random.randint(1, 10) + bonus_atak + CIOS_KRYTYCZNY
                print("DEBUG bonus:", bonus_atak)

                atak_wroga = random.randint(1, 3)

                if atak_wroga == 1:
                    obrazenia1 = random.randint(5, 10)
                    print("----------------------------------")
                    print("Ogr Marcin uderzył cię swoim mieczem i zadał ci", obrazenia1)
                    print("----------------------------------")
                elif atak_wroga == 2:
                    obrazenia1 = random.randint(1, 6)
                    print("----------------------------------")
                    print("Ogr Marcin kopnął cię i zadał ci", obrazenia1)
                    print("----------------------------------")
                elif atak_wroga == 3:
                    obrazenia1 = random.randint(5, 15)
                    print("----------------------------------")
                    print("Ogr Marcin rzucił w ciebie głazem i zadał ci", obrazenia1)
                    print("----------------------------------")
                zycie_wroga -= obrazenia
                zycie_gracza -= obrazenia1
                print("-------------")
                print("Zaatakowałeś Ogra Marcina i zadałeś mu", obrazenia, "HP")
                print("CIOS KRYTYCZNY!:", CIOS_KRYTYCZNY)
                print("Życie Ogra Marcina:", zycie_wroga)
                print("-------------")
                if zycie_wroga <= 0:
                    print("----------------------------------")
                    print("Gratulacje,pokonałeś Ogra Marcina, oraz zdobyłeś jego miecz który daje +5 do ataku!")
                    print("Znalazłeś również dziwne małe metalowe koło w kolorze świecącym szarym")
                    print("----------------------------------")
                    bonus_atak += 5
                    srebrniki += 10
                    miecz_ogra += 1
        elif wybór1 == 2:

            if zycie_wroga1 <= 0:
                print("----------------------------------")
                print("Smok Andrzej został już pokonany.")
                print("----------------------------------")
            else:
                CIOS_KRYTYCZNY = random.randint(1, 5)
                if CIOS_KRYTYCZNY == 2:
                    CIOS_KRYTYCZNY += 5
                else:
                    CIOS_KRYTYCZNY = 0
                obrazenia = random.randint(1, 10) + bonus_atak + CIOS_KRYTYCZNY
                print("DEBUG bonus:", bonus_atak)

                atak_wroga = random.randint(1, 3)

                if atak_wroga == 1:
                    obrazenia1 = random.randint(10, 15)
                    print("----------------------------------")
                    print("Smok Andrzej uderzył cię swoim swoim ogonem i zadał ci", obrazenia1)
                    print("----------------------------------")
                elif atak_wroga == 2:
                    obrazenia1 = random.randint(4, 10)
                    print("----------------------------------")
                    print("Smok Andrzej kopnął cię i zadał ci", obrazenia1)
                    print("----------------------------------")
                elif atak_wroga == 3:
                    obrazenia1 = random.randint(20, 35)
                    print("----------------------------------")
                    print("Smok Andrzej ziewnął na cibie ogniem i zadał ci", obrazenia1)
                    print("----------------------------------")
                zycie_wroga1 -= obrazenia
                zycie_gracza -= obrazenia1
                print("-------------")
                print("Zaatakowałeś Smoka Andrzeja i zadałeś mu", obrazenia, "HP")
                print("CIOS KRYTYCZNY!:", CIOS_KRYTYCZNY)
                print("Życie Smok Andrzeja:", zycie_wroga1)
                print("-------------")
                if zycie_wroga1 <= 0:
                    print("----------------------------------")
                    print("WOW!! Pokonałeś Smoka Andzreja, wygląda na to że jednak coś ppotrafisz.")
                    print("Przy smoku znalazłeś smoczy ząb i stworzyłeś z niego sztylet ze smoczego zęba. Nieźle!")
                    print("----------------------------------")
                    bonus_atak += 15
                    srebrniki += 10
                    smoczy_sztylet += 1
    elif wybór == 2:

        print("-------------")
        print("1. Wypij własnoręcznie robiony sok leczniczy")
        print("2. Wypij miksturę leczniczą")
        print("-------------")

        wybór2 = int(input("Co chcesz wypić?: "))

        if wybór2 == 1:
            leczenie = random.randint(5, 10)
            print("-------------")
            print("Wypiłeś własnoręcznie robiony sok leczniczy, i zdobyłeś", leczenie, "HP")
            zycie_gracza += leczenie
            if zycie_gracza > 100:
                zycie_gracza = 100
            print("Twoje życie", zycie_gracza)
            print("-------------")
        if wybór2 == 2:

            if zycie_wroga >= 0:
                print("-------------")
                print("Jesze nie znalazłeś tego przedmiotu.")
                print("-------------")
            else:
                leczenie1 = random.randint(10, 25)
                print("-------------")
                print("Wypiłeś miksturę leczniczą, i zdobyłeś", leczenie1, "HP")
                zycie_gracza += leczenie1
                if zycie_gracza > 100:
                    zycie_gracza = 100
                print("Twoje życie", zycie_gracza)
                print("-------------")
    elif wybór == 3:
        print("-------------")
        print("Twój bonus do ataku:", bonus_atak)
        print("Życie:", zycie_gracza, "/100")
        print("Srebrne monety:", srebrniki)
        print("Złote monety:", zlote_monety)
        print("-------------")
    elif wybór == 4:
        print("Ekwipunek gracza", nazwa, ":")
        if miecz_ogra == True:
            print("Miecz ogra +5 ataku")
        if smoczy_sztylet == True:
            print("Miecz ogra +5 ataku")
        if trolii_sztylet == True:
            print("Miecz ogra +5 ataku")
        if wilcza_wlocznia == True:
            print("Miecz ogra +5 ataku")

        if miecz_ogra == False:
            smoczy_sztylet == False
            trolii_sztylet == False
            wilcza_wlocznia == False
            print("-------------")
            print("Brak przedmiotów w ekwipunku")
            print("-------------")


    elif wybór == 5:
        print("-------------")
        print("Sklep Elfa Macieja")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 100 srebrników--")
        print("2.--Wilczy pazur--  -- +8 do ataku--  --Koszt 50 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        wybor_sklep = (input("Wybierz przedmiot który chcesz zakupić: "))
        if wybor_sklep == 1:
            if srebrniki >= 100:
                srebrniki -= 100
                bonus_atak += 10
                trolii_sztylet += 1
                print("Gratulujemy zakupu zęba trolla!")
            else:
                print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
        if wybor_sklep == 2:
            if srebrniki >= 50:
                srebrniki -= 50
                bonus_atak += 8
                wilcza_wlocznia += 1
                print("Gratulujemy zakupu wilczego pazura!")
            else:
                print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")

    elif wybór == 6:
        print("-------------")
        print("Uciekłeś, ale zobaczymy się jescze tak?.")
        break
    if zycie_gracza <= 0:
        print("Ohh,przegrałeś. Może następnym razem się uda.")

        break