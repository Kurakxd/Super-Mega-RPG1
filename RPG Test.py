import random

print("----SUPER ULTRA RPG----\n-----------------------")
print("--STWÓRZ SWOJĄ POSTAĆ--\n-----------------------")
print("1.---STWÓRZ BOHATERA---")
print("2.---STWÓRZ BOHATERA---")
print("3.---STWÓRZ BOHATERA---")

print("-----------------------")
stworz_bohatera = int(input("Wybierz zapis na którym chcesz grać: "))
print("-----------------------")

nazwa = input("Nazwij swojego bohatera: ")

print("-----------------------\nWitaj w świecie magii", nazwa, " \n-----------------------")

unik = 0
CIOS_KRYTYCZNY = 0
bonus_atak = 0
zycie_gracza = 100
zycie_wroga = 150
zycie_wroga1 = 300
srebrniki = 0
zlote_monety = 0
poziom_gracza = 0
punkty_doswiadczenia = 0

bronie = []

miecz_ogra = False
smoczy_sztylet = False
trolii_sztylet = False
wilcza_wlocznia = False
# ------------------------
uzywalne = []
wlasnorecznie_robiony_sok_leczniczy = 10
mikstura_lecznicza = 0

while True:

    if punkty_doswiadczenia == 50:
        poziom_gracza += 1
        punkty_doswiadczenia == 0

    print("1. Atak\n-------------")
    print("2. Dane gracza\nTwój bonus do ataku:", bonus_atak, "\nTwoje HP:", zycie_gracza, "/100\n-------------")
    print("3. Ekwipunek\n-------------")
    print("4. Sklep\n-------------")
    print("5. Ucieczka\n-------------")

    wybór = int(input("Proszę wpisać cyfrę odpowiadającej danej opcji: "))

    if wybór == 1:
        print("-------------\n1. Zaatakuj Ogra Marcina")
        print("2. Zatakuj Smoka Andrzeja\n!! Uwaga Smok Andrzej jest mocniejszym przeciwnikiem od Ogra Marcina !!\n-------------")

        wybór1 = int(input("Kogo chcesz zaatakować?: "))

        if wybór1 == 1:

            if zycie_wroga <= 0:
                print("----------------------------------\nOgr Marcin został już pokonany.\n----------------------------------")
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
                    print("----------------------------------\nOgr Marcin uderzył cię swoim mieczem i zadał ci", obrazenia1, "\n----------------------------------")
                elif atak_wroga == 2:
                    obrazenia1 = random.randint(1, 6)
                    print("----------------------------------\nOgr Marcin kopnął cię i zadał ci", obrazenia1, "\n----------------------------------")
                elif atak_wroga == 3:
                    obrazenia1 = random.randint(5, 15)
                    print("----------------------------------\nOgr Marcin rzucił w ciebie głazem i zadał ci", obrazenia1, "\n----------------------------------")
                zycie_wroga -= obrazenia
                zycie_gracza -= obrazenia1
                print("-------------\nZaatakowałeś Ogra Marcina i zadałeś mu", obrazenia, "HP")
                print("CIOS KRYTYCZNY!:", CIOS_KRYTYCZNY)
                print("UNIK!:", unik)
                if unik == 1:
                    print("Uniknąłeś ataku")
                print("Życie Ogra Marcina:", zycie_wroga)
                print("-------------")
                if zycie_wroga <= 0:
                    print("----------------------------------")
                    print("Gratulacje,pokonałeś Ogra Marcina, oraz zdobyłeś jego miecz który daje +5 do ataku!")
                    print("Znalazłeś również dziwne małe metalowe koło w kolorze świecącym szarym")
                    print("----------------------------------")
                    bonus_atak += 5
                    mikstura_lecznicza += 5
                    srebrniki += 50
                    punkty_doswiadczenia += 50
                    miecz_ogra = True
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
                    srebrniki += 100
                    smoczy_sztylet = True
    elif wybór == 2:
        print("-------------")
        print("Poziom doświadczenia gracza", nazwa, ":", poziom_gracza)
        print("Twój bonus do ataku:", bonus_atak)
        print("Życie:", zycie_gracza, "/100")
        print("Srebrniki:", srebrniki)
        print("Złote monety:", zlote_monety)
        print("-------------")
    elif wybór == 3:
        print("Ekwipunek gracza", nazwa, ":")
        print("1. Bronie")
        print("2. Używalne")

        wybor_eq = int(input("Wybierz którą kategorie ekwipunku chcesz zobaczyć: "))
        if wybor_eq == 1:
            print("Bronie:")
            if miecz_ogra == True:
                print("Miecz ogra +5 ataku")
            if smoczy_sztylet == True:
                print("Smoczy sztylet +15 ataku")
            if trolii_sztylet == True:
                print("Trolli sztylet +10 ataku")
            if wilcza_wlocznia == True:
                print("Wilcza włócznia +8 ataku")
            if miecz_ogra == False:
                smoczy_sztylet == False
                trolii_sztylet == False
                wilcza_wlocznia == False
                print("-------------")
                print("Brak przedmiotów w tek kategorii")
                print("-------------")
        if wybor_eq == 2:
            print("Używalne: ")

            print("-------------")
            print("1. Wypij własnoręcznie robiony sok leczniczy, ilość:", wlasnorecznie_robiony_sok_leczniczy)
            print("2. Wypij miksturę leczniczą, ilość:", mikstura_lecznicza)
            print("3. Powrót")
            print("-------------")

            wybór2 = int(input("Co chcesz wypić?: "))

            if wybór2 == 1:
                if zycie_gracza == 100:
                    print("-------------")
                    print("Twój bohater ma już zapełniony pasek zdrowia")
                    print("-------------")
                else:
                    leczenie = random.randint(5, 10)
                    print("-------------")
                    print("Wypiłeś własnoręcznie robiony sok leczniczy, i zdobyłeś", leczenie, "HP")
                    wlasnorecznie_robiony_sok_leczniczy -= 1
                    zycie_gracza += leczenie
                    if zycie_gracza > 100:
                        zycie_gracza = 100
                    print("Twoje życie", zycie_gracza)
                    print("-------------")
            elif wybór2 == 2:

                if zycie_wroga >= 0:
                    print("-------------")
                    print("Jesze nie znalazłeś tego przedmiotu.")
                    print("-------------")
                else:
                    if zycie_gracza == 100:
                        print("-------------")
                        print("Twój bohater ma już zapełniony pasek zdrowia")
                        print("-------------")
                    else:
                        leczenie1 = random.randint(10, 25)
                        print("-------------")
                        print("Wypiłeś miksturę leczniczą, i zdobyłeś", leczenie1, "HP")
                        mikstura_lecznicza -= 1
                        zycie_gracza += leczenie1
                        if zycie_gracza > 100:
                            zycie_gracza = 100
                        print("Twoje życie", zycie_gracza)
                        print("-------------")
            elif wybór2 == 3:
                print("-------------")

    elif wybór == 4:
        print("-------------")
        print("Sklep Elfa Macieja")
        print("1.--Ząb trola--  -- +10 do ataku--  --Koszt 100 srebrników--")
        print("2.--Wilczy pazur--  -- +8 do ataku--  --Koszt 50 srebrników--")
        print("3.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("4.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("5.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("6.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("7.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("8.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("9.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
        print("10. Powrót")
        wybor_sklep = int(input("Wybierz przedmiot który chcesz zakupić: "))
        if wybor_sklep == 1:
            if srebrniki >= 100:
                srebrniki -= 100
                bonus_atak += 10
                trolii_sztylet = True
                print("Gratulujemy zakupu zęba trolla!")
            else:
                print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
        elif wybor_sklep == 2:
            if srebrniki >= 50:
                srebrniki -= 50
                bonus_atak += 8
                wilcza_wlocznia = True
                print("Gratulujemy zakupu wilczego pazura!")
            else:
                print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
        elif wybor_sklep == 10:
            print("-------------")
            print("Do zobacznie póżniej")
            print("-------------")

    elif wybór == 5:
        print("-------------")
        print("Uciekłeś, ale zobaczymy się jescze tak?.")
        break
    if zycie_gracza <= 0:
        print("Ohh,przegrałeś. Może następnym razem się uda.")

        break
