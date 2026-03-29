import random
from games.dice import dice_game


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

do_nastepnego_poziomu = 50
punkty_doswiadczenia = 0
poziom_doswiadczenia = 0
unik = 0
CIOS_KRYTYCZNY = 0
bonus_atak = 0
bonus_życie = 0
zycie_gracza = 100 + bonus_życie
zycie_wroga = 1
zycie_wroga1 = 300
srebrniki = 0
zlote_monety = 0
mnoznik_cen = 1.0
dlug_u_Macieja = 0
tura = 0
proba_zgadnij_liczbe = 0
mnoznik_zgadnij_liczbe = 1
poziom_sily = 0
poziom_energii = 0
poziom_charyzmy = 0
punkty_sec = 11
mnoznik_cen_z_charyzma = 1.0

losowe_przypadki = []

dziwny_npc_byl = False
# ------------------------
gry = []

gra_w_liczbe_zaczeta = False
# ------------------------
statystyki = []

klamca_zadanie_z_ogrem = False
samouczek_ukonczony = False
# ------------------------
sklep = []

wrocil_klamca = False
wrocil_klamca_po = False
# ------------------------
zadania = []

zadanie_z_ogrem = False
zadanie_z_ogrem_aktywne = True
anty_zadanie_z_ogrem_opcja2 = False
zadanie_z_ogrem_zaakceptowane = False
zadanie_z_ogrem_skończone = False
anty_zadanie_z_ogrem_powrot = False
# ------------------------
bronie = []

miecz_ogra = False
smoczy_sztylet = False
trolii_sztylet = False
wilcza_wlocznia = False
miecz_z_skały_Emiti = False
# ------------------------
wyposazenie = []
zbroja_ogra = False
smoczy_pancerz = False
kosciany_pancerz = False
miedziana_zbroja = False
# ------------------------
uzywalne = []
wlasnorecznie_robiony_sok_leczniczy = 10
mikstura_lecznicza = 0

while True:
    if poziom_charyzmy == 1:
        mnoznik_cen_z_charyzma = 0.95
    if poziom_charyzmy == 2:
        mnoznik_cen_z_charyzma = 0.9
    if poziom_charyzmy == 3:
        mnoznik_cen_z_charyzma = 0.85
    if poziom_charyzmy == 4:
        mnoznik_cen_z_charyzma = 0.8
    if poziom_charyzmy == 5:
        mnoznik_cen_z_charyzma = 0.75
    if poziom_charyzmy == 6:
        mnoznik_cen_z_charyzma = 0.7
    if poziom_charyzmy == 7:
        mnoznik_cen_z_charyzma = 0.65
    if poziom_charyzmy == 8:
        mnoznik_cen_z_charyzma = 0.6
    if poziom_charyzmy == 9:
        mnoznik_cen_z_charyzma = 0.55
    if poziom_charyzmy == 10:
        mnoznik_cen_z_charyzma = 0.5

    # ------------------------
    zab_trola_c = int(100 * mnoznik_cen * mnoznik_cen_z_charyzma)
    wilczy_pazur_c = int(50 * mnoznik_cen * mnoznik_cen_z_charyzma)
    # ------------------------
    kosciany_pancerz_c = int(35 * mnoznik_cen * mnoznik_cen_z_charyzma)
    miedziana_zbroja_c = int(80 * mnoznik_cen * mnoznik_cen_z_charyzma)
    # ------------------------
    if punkty_doswiadczenia >= do_nastepnego_poziomu:
        poziom_doswiadczenia += 1
        punkty_doswiadczenia -= do_nastepnego_poziomu
        do_nastepnego_poziomu += 100
        punkty_sec += 2

    if samouczek_ukonczony is False:
        print("Czy przed startem chcesz zobaczyć samouczek?")
        print("1. Tak")
        print("2. Nie")
        wybor_samouczek = int(input("Wybierz opcję: "))
        if wybor_samouczek == 1:
            print("Okej zaczynajmy!")
            print("1. Wyprawa, dzięki tej funkcji bohater może zaatakować jakąś postać lub odbyć wędrówkę i potencjalnie"
                "odkryć nowe miejsca lub spotakć postacie")
            print("----------------------------------")
            print("2. Dane gracza, w tej zakładce możemy sprawdzić wszytkie dane na temat naszej postaci np. ilość HP"
                "ilość bonusu do ataku czy ilość srebrników")
            print("----------------------------------")
            print("3. Ekwipunek, tam możem sprawdzić jakie gracz ma bronie, zbroje czy sprawdzić ilość mikstur leczących i"
                "je użyć")
            print("----------------------------------")
            print("4. S.E.C, czyli Siła.Energia.Charyzma, dzięki sile wzrasta ilość bonusu do atak, enrgia zwiększa życie "
                "maksymalne gracza, a im większy poziom charyzmy ma gracz tam tańsze reczy będą w sklepach.")
            print("----------------------------------")
            print("5. Sklep Elfa Macieja, w ty miesjcu można kupić bronie, zbroje oraz leczenie, ale można również"
                "zaakceptować zadania, za których wykonanie będzie nagroda")
            print("----------------------------------")
            print("6. Centrum gier Handlarza Marka, w tym miejscu możemy grać w różne gry używając srebrników, znajdują "
                "się tam gry takie jak: Gra w Kości, Zgadnij Liczbę i Wyższa Karta. Można to miejsce nazwać kasynem.")
            print("----------------------------------")
            print("7. Ucieczka, jest to funkcja dzięki której użytkownik może opuścic grę.")
            print("----------------------------------")
            print("1. Zacznij grę")
            print("----------------------------------")
            samouczek_koniec = int(input("Wybierz opcję: "))
        else:
            print()

    print("---MIASTECZKO BOGO---")
    print("1. Wyprawa\n-------------")
    print("2. Dane gracza\nTwój bonus do ataku:", bonus_atak, "\nTwoje HP:", zycie_gracza, "/ 100""\nDzień:", tura,
          "\n-------------")
    print("3. Ekwipunek\n-------------")
    print("4. S.E.C\n-------------")
    print("5. Sklep Elfa Macieja\n-------------")
    print("6. Centrum gier Handlarza Marka\n-------------")
    print("7. Ucieczka\n-------------")

    wybór = int(input("Proszę wpisać cyfrę odpowiadającej danej opcji: "))

    if wybór == 1:
        samouczek_ukonczony = True
        tura += 1
        print("1. Zaatakuj postać")
        print("2. Eksploruj świat")
        print("3. Powrót")

        wybór_wyprawa = int(input("Wybierz opcje: "))

        if wybór_wyprawa == 1:
            print("-------------\n1. Zaatakuj Ogra Marcina")
            print(
                "2. Zatakuj Smoka Andrzeja\n!! Uwaga Smok Andrzej jest mocniejszym przeciwnikiem od Ogra Marcina "
                "!!\n-------------")

            wybór1 = int(input("Kogo chcesz zaatakować?: "))

            if wybór1 == 1:

                if zycie_wroga <= 0:
                    print(
                        "----------------------------------\nOgr Marcin został już pokonany.\n----------------------------------")
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
                        print("----------------------------------\nOgr Marcin uderzył cię swoim mieczem i zadał ci",
                              obrazenia1, "\n----------------------------------")
                    elif atak_wroga == 2:
                        obrazenia1 = random.randint(1, 6)
                        print("----------------------------------\nOgr Marcin kopnął cię i zadał ci", obrazenia1,
                              "\n----------------------------------")
                    elif atak_wroga == 3:
                        obrazenia1 = random.randint(5, 15)
                        print("----------------------------------\nOgr Marcin rzucił w ciebie głazem i zadał ci",
                              obrazenia1, "\n----------------------------------")
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
                        punkty_doswiadczenia += 50
                        bonus_życie += 10
                        bonus_atak += 5
                        mikstura_lecznicza += 5
                        srebrniki += 50
                        miecz_ogra = True
                        zbroja_ogra = True
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
                        punkty_doswiadczenia += 100
                        bonus_życie += 20
                        bonus_atak += 15
                        srebrniki += 100
                        smoczy_sztylet = True
                        smoczy_pancerz = True
        elif wybór_wyprawa == 2:
            print("1. Zacznij eksplorować")
            print("2. Wróć do miasteczka Bogo")
            wybór_exsploracja = int(input("Wybierz opcję: "))
            if wybór_exsploracja == 1:
                wydarzenie = random.randint(3, 3)
                if wydarzenie == 1:
                    srebrniki_ilosc = random.randint(10, 30)
                    print(f"Znalazłeś skrzynie w której było {srebrniki_ilosc} srebrników")
                    srebrniki += srebrniki_ilosc
                    print("1. Powrót")
                    interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))
                if wydarzenie == 2:
                    print("Zaatakowało cię 10 mocno uzbrojonych bandytów.")
                    zycie_gracza_atak_bandytow = random.randint(5, 15)
                    srebrniki_zabrane = random.randint(10, 20)
                    print(f"Zabrali ci {srebrniki_zabrane} i zadali ci {zycie_gracza_atak_bandytow} HP")
                    srebrniki -= srebrniki_zabrane
                    zycie_gracza -= zycie_gracza_atak_bandytow
                if wydarzenie == 3 and dziwny_npc_byl is False:
                    print("Spotkałeś dziwnego sprzedawcę.")
                    print("-------------")
                    print("CHCESZ KUPIĆ FAJNĄ RZECZ ODEMNIE ZA 20 SREBRNIKÓW?")
                    print("1. Tak")
                    print("2. Nie")
                    interakcja_dziwny_npc = int(input("Wybierz opcję: "))
                    if interakcja_dziwny_npc == 1:
                        if srebrniki > 20:
                            print("NO I SUPER TRZYMAJ!")
                            print("Otrzymałeś miecz stworzony z legendarjne skały Emiti")
                            print("1. Powrót")
                            miecz_z_skały_Emiti = True
                            dziwny_npc_byl = True
                            interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))
                        else:
                            print("PRÓBUJESZ MNIE OSZUKAĆ JAK ŚMIESZ!")
                            zycie_gracza -= 999
                            zycie_gracza += 1
                            print("Co się stało?")
                            print("1. Powrót")
                            dziwny_npc_byl = True
                            interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))
                    elif interakcja_dziwny_npc == 2:
                        print("TWOJA STARTA")
                        dziwny_npc_byl = True
                        print("1. Powrót")
                        interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))
                if wydarzenie == 4:
                    skrzynia_mikstura = random.randint(1, 5)
                    print(f"Znalazłeś skrzynie z {skrzynia_mikstura} miksturami leczniczymy")
                    mikstura_lecznicza += skrzynia_mikstura
                    print("1. Powrót")
                    interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))
                if wydarzenie == 5:
                    print("Nic podczas wyprawy się nie stało")
                    print("1. Powrót")
                    interakcja_dziwny_npc_wybor = int(input("Wybierz opcję: "))

            else:
                print("-------------")
                print("Wróciłeś do miasteczka Bogo")
                print("-------------")
        elif wybór_wyprawa == 3:
            print("-------------")
            print("Wróciłeś do miasteczka Bogo")
            print("-------------")
    elif wybór == 2:
        samouczek_ukonczony = True
        tura += 1
        print("-------------")
        print("Poziom doświadczenia gracza", nazwa, ":", poziom_doswiadczenia)
        print("Punkty doświadczenia gracza", nazwa, ":", punkty_doswiadczenia)
        print("Twój bonus do ataku:", bonus_atak)
        print("Życie:", zycie_gracza, "/100")
        print("Srebrniki:", srebrniki)
        print("Złote monety:", zlote_monety)
        print("-------------")
    elif wybór == 3:
        samouczek_ukonczony = True
        tura += 1
        print("Ekwipunek gracza", nazwa, ":")
        print("1. Bronie")
        print("2. Wyposażenie")
        print("3. Używalne")
        print("4. Powrót")

        wybor_eq = int(input("Wybierz którą kategorie ekwipunku chcesz zobaczyć: "))
        if wybor_eq == 1:
            print("Bronie:")
            if miecz_ogra is True:
                print("Miecz ogra +5 ataku")
            if smoczy_sztylet is True:
                print("Smoczy sztylet +15 ataku")
            if trolii_sztylet is True:
                print("Trolli sztylet +10 ataku")
            if wilcza_wlocznia is True:
                print("Wilcza włócznia +8 ataku")
            if miecz_z_skały_Emiti is True:
                print("Miecz z skały Emiti +20 ataku")
            if miecz_ogra is False and smoczy_sztylet is False and trolii_sztylet is False and wilcza_wlocznia is False and miecz_z_skały_Emiti is False:
                print("-------------")
                print("Brak przedmiotów w tek kategorii")
                print("-------------")
        if wybor_eq == 2:
            print("Wyposażenie")
            if zbroja_ogra is True:
                print("Zbroja ogra + 10 do HP")
            if smoczy_pancerz is True:
                print("Smoczy pancerz + 20 do HP")
            if zbroja_ogra is False and smoczy_pancerz is False:
                print("-------------")
                print("Brak przedmiotów w tek kategorii")
                print("-------------")

        if wybor_eq == 3:
            print("Używalne: ")

            print("-------------")
            print("1. Wypij własnoręcznie robiony sok leczniczy, ilość:", wlasnorecznie_robiony_sok_leczniczy)
            print("2. Wypij miksturę leczniczą, ilość:", mikstura_lecznicza)
            print("3. Powrót")
            print("-------------")

            wybór2 = int(input("Co chcesz wypić?: "))

            if wybór2 == 1:
                if zycie_gracza == 100 + bonus_życie:
                    print("-------------")
                    print("Twój bohater ma już zapełniony pasek zdrowia")
                    print("-------------")
                else:
                    leczenie = random.randint(5, 10)
                    print("-------------")
                    print("Wypiłeś własnoręcznie robiony sok leczniczy, i zdobyłeś", leczenie, "HP")
                    wlasnorecznie_robiony_sok_leczniczy -= 1
                    zycie_gracza += leczenie
                    if zycie_gracza > 100 + bonus_życie:
                        zycie_gracza = 100 + bonus_życie
                    print("Twoje życie", zycie_gracza)
                    print("-------------")
            elif wybór2 == 2:

                if zycie_wroga >= 0:
                    print("-------------")
                    print("Jesze nie znalazłeś tego przedmiotu.")
                    print("-------------")
                else:
                    if zycie_gracza == 100 + bonus_życie:
                        print("-------------")
                        print("Twój bohater ma już zapełniony pasek zdrowia")
                        print("-------------")
                    else:
                        leczenie1 = random.randint(10, 25)
                        print("-------------")
                        print("Wypiłeś miksturę leczniczą, i zdobyłeś", leczenie1, "HP")
                        mikstura_lecznicza -= 1
                        zycie_gracza += leczenie1
                        if zycie_gracza > 100 + bonus_życie:
                            zycie_gracza = 100 + bonus_życie
                        print("Twoje życie", zycie_gracza)
                        print("-------------")
            elif wybór2 == 3:
                print("-------------")
        if wybor_eq == 4:
            print("------------------")
    elif wybór == 4:
        samouczek_ukonczony = True
        print("----S.E.C-----")
        print("1. Siła")
        print(f"Poziom Siły:{poziom_sily} ")
        print("Siła zwiększa ilość zadawanych obrażeń przez twojego bohatera bez względu na wyposażoną broń")
        print("-------------")
        print("2. Energia")
        print(f"Poziom Energii:{poziom_energii} ")
        print("Energia zwiększa ilość punktó zdrowia twojego bohatera.")
        print("-------------")
        print("3. Charyzma")
        print(f"Poziom Charyzmy:{poziom_charyzmy} ")
        print("Charyzma pozwala ci wynegocjować lepsze ceny u handlarzy.")
        print("-------------")
        print("4. Powrót")
        print("-------------")
        print(f"Masz {punkty_sec} punktów S.E.C do wydania")
        wybor_sec = int(input("Wybierz opcję: "))
        if wybor_sec == 1:
            if punkty_sec >= 0:
                print("Gratulacje twój poziom siły wzrósł o 1 poziom. Zdobyłeś +5 do ataku")
                bonus_atak += 5
                punkty_sec -= 1
                if poziom_sily > 10:
                    poziom_sily = 10
                    print("Osiągnięto maksymalny poziom siły")
            else:
                print("Brak punktów S.E.C do wydania")
        if wybor_sec == 2:
            if punkty_sec >= 0:
                print("Gratulacje twój poziom energii wzrósł o 1 poziom. Zdobyłeś +10 punktów zdrowia")
                bonus_życie += 10
                punkty_sec -= 1
                if poziom_energii > 10:
                    poziom_energii = 10
                    print("Osiągnięto maksymalny poziom energii")
            else:
                print("Brak punktów S.E.C do wydania")
        if wybor_sec == 3:
            if punkty_sec >= 0:
                print("Gratulacje twój poziom charyzmy wzrósł o 1 poziom. Zdobyłeś +1 punkt charyzmy")
                poziom_charyzmy += 1
                punkty_sec -= 1
                if poziom_charyzmy > 10:
                    poziom_charyzmy = 10
                    print("Osiągnięto maksymalny poziom charyzmy")
            else:
                print("Brak punktów S.E.C do wydania")
        if wybor_sec == 4:
            print("-------")

    elif wybór == 5:
        samouczek_ukonczony = True
        tura += 1
        if klamca_zadanie_z_ogrem is True and wrocil_klamca_po is False:
            wrocil_klamca_po = True
            print("Prosze, prosze, prosze, kto tu się pojawił? Uwież mi kłamanie to był serio słaby ruch. SERIO!")
            print("Szczerze po tobie spodziewałem się więcej, ale no to co się stało się nie odbędzie.")
            print("Z racji, że chciałeś zgarnać darmowe 50 srebrników, specjalnie dla ciebie podniosę wszytkie ceny.")
            print("Ale spokojnie jeżeli oddasz mi 50 srebrników i 30 srebrników kary, powiedzmy, że zapomne o sprawie")
            print("1. Spłać dług ")
            print("2. Daj mi chwilę")
            dług_dialog = int(input("Wybierz opcję: "))
            if dług_dialog == 1:
                if srebrniki >= 80:
                    srebrniki -= 80
                    dlug_u_Macieja = 0
                    mnoznik_cen = 1.0
                    print("No i super, dług spłacony a ceny wracają do normy.")
                else:
                    print("Nie próbuj mnie oszukiwać drugi raz bo źle to się skończy.")
            elif dług_dialog == 2:
                print("Jasne, ale pamiętaj że do tego czasu ceny są podniesione.")
        if wrocil_klamca_po == True:
            print("Pamiętaj wciaż masz dług do spłacenia")

        print("-------------")
        print("Sklep Elfa Macieja")
        print("PROMOCJA CO KAŻDE 10 DNI")
        print("1. Bronie")
        print("2. Wyposażenie")
        print("3. Zadanie")
        print("4. Powrót")
        wybor_sklep = int(input("Któą kategorię chcesz odwiedzić? : "))

        if wybor_sklep == 1:
            print(f"1.--Ząb trola--  -- +10 do ataku--  --Koszt {zab_trola_c} srebrników--")
            print(f"2.--Wilczy pazur--  -- +8 do ataku--  --Koszt {wilczy_pazur_c} srebrników--")
            print(f"3.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"4.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"5.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"6.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"7.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"8.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"9.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print("10. Powrót")
            wybor_sklep_bronie = int(input("Wybierz opcję: "))
            if wybor_sklep_bronie == 1:
                if srebrniki >= 100:
                    srebrniki -= 100
                    bonus_atak += 10
                    trolii_sztylet = True
                    print("Gratulujemy zakupu zęba trolla!")
                else:
                    print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
            elif wybor_sklep_bronie == 2:
                if srebrniki >= 50:
                    srebrniki -= 50
                    bonus_atak += 8
                    wilcza_wlocznia = True
                    print("Gratulujemy zakupu wilczego pazura!")
                else:
                    print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
            elif wybor_sklep_bronie == 10:
                print("Do zobaczenia póżniej")
        elif wybor_sklep == 2:
            print(f"1.--Kościany pancerz--  -- +15 HP--  --Koszt {kosciany_pancerz_c} srebrników--")
            print(f"2.--Miedziana zbroja--  -- +25 HP--  --Koszt {miedziana_zbroja_c} srebrników--")
            print(f"3.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"4.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"5.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"6.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"7.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"8.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"9.--Ząb trola--  -- +10 do ataku--  --Koszt 10 srebrników--")
            print(f"10. Powrót")
            wybor_sklep_wyposazenie = int(input("Wybierz opcję: "))
            if wybor_sklep_wyposazenie == 1:
                if srebrniki >= 35:
                    srebrniki -= 35
                    bonus_życie += 15
                    kosciany_pancerz = True
                    print("Gratulujemy zakupu kościanego pancerza!")
                else:
                    print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
            elif wybor_sklep_wyposazenie == 2:
                if srebrniki >= 80:
                    srebrniki -= 80
                    bonus_życie += 25
                    miedziana_zbroja = True
                    print("Gratulujemy zakupu miedzianej zbrojii!")
                else:
                    print("Nie masz wystarczająco srebrników, wpadnij następnym razem jak je zdobędziesz")
            elif wybor_sklep_wyposazenie == 10:
                print("Do zobaczenia póżniej")
        elif wybor_sklep == 3:
            anty_zadanie_z_ogrem_powrot = False
            if zadanie_z_ogrem_aktywne == True:
                if zadanie_z_ogrem == True:
                    print("Witaj z powrotem! Ukończyłeś swoje zadanie?")
                    print("1. Tak")
                    print("2. Nie")
                    print("3. Daj mi jescze chwilę")
                    zadanie_z_ogrem_CH = int(input("Wybierz opcję: "))
                    if zadanie_z_ogrem_CH == 1:
                        if zycie_wroga <= 0:
                            print("-------------")
                            print("Wiedziałem, że dasz radę. Proszę o to twoje 50 srebrników.")
                            print("-------------")
                            srebrniki += 50
                            zadanie_z_ogrem = False
                            anty_zadanie_z_ogrem_opcja2 = True
                            anty_zadanie_z_ogrem_powrot = True
                        if zycie_wroga >= 0:
                            print("-------------")
                            print("Wiedziałem, że dasz radę. Proszę o to twoje 50 srebrników.")
                            print("-------------")
                            srebrniki += 50
                            zadanie_z_ogrem = False
                            klamca_zadanie_z_ogrem = True
                            anty_zadanie_z_ogrem_opcja2 = True
                            anty_zadanie_z_ogrem_powrot = True
                            dlug_u_Macieja = 80
                            mnoznik_cen = 1.5
                    if zadanie_z_ogrem_CH == 2:
                        print("-------------")
                        print(
                            "Nie żeby coś ale jak tego szybko nie zrobisz to nagroda przepadnie więc miej to na uwadze.")
                        print("-------------")
                    if zadanie_z_ogrem_CH == 3:
                        print("-------------")
                        print("Jasne, ale pamiętaj, że nie masz nie ograniczonego czasu")
                        print("-------------")
                if zycie_wroga >= 0 and zadanie_z_ogrem_zaakceptowane == False:
                    print(
                        "Okej chcesz wyzwania i zgarnąć troche srebrników? W takim razie pokonaj dla mnie Ogra Marcina.")
                    print("Płace 50 srebrników, serio dobra sumka")
                    print("-------------")
                    print("1. Przyjmij")
                    print("2. Wróć do tego póżniej")
                    wybor_zadanie = int(input("Wybierz opcję: "))
                    if wybor_zadanie == 1:
                        print("-------------")
                        print("No i świetnie wróć do mnie jak skończysz")
                        zadanie_z_ogrem = True
                        zadanie_z_ogrem_zaakceptowane = True
                    elif wybor_zadanie == 2:
                        print("-------------")
                        print("Dobrze, ale nie gwarantuje, że oferta będzie jak wrócisz.")
                if zycie_wroga <= 0 and anty_zadanie_z_ogrem_opcja2 == False:
                    print("-------------")
                    print(
                        "Hmmm wykonałeś zadanie które miałem komuś powierzyć, słuchaj ponieważ mam troche ich masz w nagrodę 25 srebrników.")
                    print(
                        "Widzę też, że tawrda z ciebie sztuka. Słuchaj zaglądaj do mnie czasami to może będe miał kolejne zadanie.")
                    print("-------------")
                    print("1. Powrót")
                    powrot_zadanie = int(input("Wybierz opcję: "))
            if zadanie_z_ogrem == False and anty_zadanie_z_ogrem_powrot == False:
                print("-------------")
                print("Obecnie nie mam żadnych zadań dla ciebie.")
                print("1. Powrót")
                print("-------------")
                zadanie_z_ogrem_powrot = int(input("Wybierz opcję: "))
        elif wybor_sklep == 4:
            print("Do zobaczenia pozniej")

    elif wybór == 6:
        samouczek_ukonczony = True
        tura += 1
        print("Centrum gier Handlarza Marka")
        print("1. Gra w kości")
        print("2. Wyższa karta")
        print("3. Zgadnij liczbe")
        print("4. Sloty")
        centrum_gier_wybor = int(input("Wybierz grę w którą chcesz zagrać: "))
        if centrum_gier_wybor == 1:
            suma_handlarz = 0
            suma_gracz = 0
            wynik1, grafika_kostki1 = dice_game.roll_dice()
            wynik2, grafika_kostki2 = dice_game.roll_dice()
            dice_game.print_two_dice(grafika_kostki1, grafika_kostki2)
            dice_game.print_result(wynik1, wynik2)
            winner = dice_game.get_winner(wynik1, wynik2)
        #     print(
        #         "1. Rozpocznij\n !!! Uwaga klikając Rozpocznij automatycznie zostanie pobrane 10 srebrników z twojego konta !!!")
        #     print("2. Powrót")
        #     gra_w_kosci_wybor = int(input("Wybierz opcje: "))
        #     if gra_w_kosci_wybor == 1:
        #         if srebrniki >= 10:
        #             srebrniki -= 10
        #             wybór_handlarza = random.randint(1, 6)
        #             print(
        #                 "Zasady gry: \n Ty wybierasz ilość oczek na kostce i zapisujesz tą liczbę aby wygrać kostka którą rzucę musi wylądować twoją liczbą do góry.")
        #             print(
        #                 "Jeżeli przegrasz jak już wiesz tracisz swoje 10 srebrników, jeżeli wygrasz odzyskujesz 10 srebrników i zyskujesz 10 ekstra.")
        #             print("---------------------------------------------------------------------------------")
        #             print("Wybierz liczbę:\n1.-1-\n2.-2-\n3.-3-\n4.-4-\n5.-5-\n6.-6-")
        #             wybór_kosci = int(input("Wybierz cyfrę:"))
        #             print(wybór_handlarza)
        #             if wybór_kosci == wybór_handlarza:
        #                 print("Gratulacje wygrałeś i zdobywasz 20 srebrników")
        #                 srebrniki += 20
        #             else:
        #                 print("Ajjj niestety przegrałeś.")
        #         else:
        #             print("Nie masz wystarczająco srebrników wróć następnym razem jak je uzbierasz")
        #     elif gra_w_kosci_wybor == 2:
        #         print("-------------")
        #         print("W takim razie dozobaczenia?")
        #         print("-------------")
        if centrum_gier_wybor == 2:
            print("1. Rozpocznij")
            print("2. Powrót")
            gra_w_karty_wybor = int(input("Wybierz opcję: "))
            if gra_w_karty_wybor == 1:
                print(
                    "Zasady gry: \n-------------\nJa wybieram kartę dla siebie i dla ciebie abyś wygrał obie karty muszą mieć taką samą liczbę.")
                print(
                    "Jeżeli przegrasz jak już wiesz tracisz swoje srebrniki, jeżeli wygrasz dostajesz swoje srebrniki z lekkim bonusem zależacym od ilości postawionych srebrników")
                print("-------------")
                stawka  = int(input("Podaj ile srebrników chcesz postawić: "))
                if srebrniki >= stawka:
                    srebrniki -= stawka
                    print("-------------")
                    print(f"Postawiłeś {stawka} srebrników. Powodzenia!")
                    karty_handlarz = random.randint(1, 20)
                    karty_gracz = random.randint(1, 20)
                    print("-------------")
                    print("Karta Handlarza:", karty_handlarz)
                    print("Twoja Karta:", karty_gracz)
                    print("-------------")
                    if karty_handlarz == karty_gracz:
                        wygrana = stawka * 1.5
                        srebrniki += wygrana
                        print(f"No gratulacje wygrałeś! Zgarniasz {wygrana} srebrników.")
                        print("-------------")
                    else:
                        print(f"Ajjjj niestety przegrałeś swoje {stawka} srebrników.")
                        print("-------------")

                else:
                    print("Z tego co widzę nie masz tyle. Czy ty próbujesz mnie oszukać?")
                    print("1. Powrót")
                    powrot_karty = int(input("Wybierz opcję: "))
        if centrum_gier_wybor == 3:
                print("1. Rozpocznij")
                print("2. Powrót")
                gra_w_karty_wybor = int(input("Wybierz opcję: "))
                if gra_w_karty_wybor == 1:
                    print("Zasady gry: \n-------------\nJa wybieram liczbę i ją zapisuje na kartce.")
                    print(
                        "Jeżeli przegrasz jak już wiesz tracisz swoje srebrniki, jeżeli wygrasz dostajesz swoje srebrniki z lekkim bonusem zależacym od ilości postawionych srebrników")
                    print("-------------")
                    stawka1 = int(input("Podaj ile srebrników chcesz postawić: "))
                if srebrniki >= stawka1:
                    srebrniki -= stawka1
                    print("-------------")
                    print(f"Postawiłeś {stawka1} srebrników. Powodzenia!")
                    gra_w_liczbe_zaczeta = True

                    if proba_zgadnij_liczbe == 1:
                        mnoznik_zgadnij_liczbe = 5
                    if proba_zgadnij_liczbe == 2:
                        mnoznik_zgadnij_liczbe = 4
                    if proba_zgadnij_liczbe == 3:
                        mnoznik_zgadnij_liczbe = 3
                    if proba_zgadnij_liczbe == 4:
                        mnoznik_zgadnij_liczbe = 2
                    if proba_zgadnij_liczbe == 5:
                        mnoznik_zgadnij_liczbe = 1.5

                    liczba_handlarz = random.randint(1, 2)
                    print("Wybierz wpisz liczbę od 1 do 50")
                    liczba_gracz = int(input("Wybierz liczbę: "))
                    print("Liczba handlarza:", liczba_handlarz)

                    if proba_zgadnij_liczbe == 6:
                        print(f"Ajjj niestety przegrywasz swoje {stawka1} srebrników")

                    if liczba_gracz == liczba_handlarz:
                        wygrana1 = stawka1 * mnoznik_zgadnij_liczbe
                        print(f"No gratulacje wygrałeś! Zgarniasz {wygrana1} srebrników.")
                        print("-------------")
                    elif liczba_gracz < liczba_handlarz:
                        print("Liczba jest za mała.")
                        proba_zgadnij_liczbe += 1
                        continue
                    elif liczba_gracz > liczba_handlarz:
                        print("Liczba jest za duża.")
                        proba_zgadnij_liczbe += 1
                        continue
                else:
                    print("Z tego co widzę nie masz tyle. Czy ty próbujesz mnie oszukać?")
                    print("1. Powrót")
                    powrot_karty = int(input("Wybierz opcję: "))


    elif wybór == 7:
        print("-------------")
        print("Uciekłeś, ale zobaczymy się jescze tak?.")
        break
    if zycie_gracza <= 0:
        print("Ohh,przegrałeś. Może następnym razem się uda.")

        break
