print("----SUPER ULTRA MEGA MENU----")
# 1233131231312312312312312312313132131111111111111111111111111111111111111111111111111111111133331111111113333333333333
while True:

    print("1. Kalkulator")
    print("2. Zgadnij liczbę")
    print("3. Logowanie")
    print("4. RPG")
    print("5. Quiz")
    print("6. Wyjście")

    opcja1 = int(input("Proszę wpisać cyfrę odpowiadającej danej opcji: "))

    if opcja1 == 1:
        print("-------------")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Potęgowanie")

        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        dzialanie = input("Wybierz działanie: ")

        if dzialanie == "1":
            print("-------------")
            print("Wynik =", a + b)
            print("-------------")
        elif dzialanie == "2":
            print("-------------")
            print("Wynik =", a - b)
            print("-------------")
        elif dzialanie == "3":
            print("-------------")
            print("Wynik =", a * b)
            print("-------------")
        elif dzialanie == "4":
            if b == 0:
                print("-------------")
                print("Nie dziel przez zero!")
                print("-------------")
            else:
                print("-------------")
                print("Wynik =", a / b)
                print("-------------")
        elif dzialanie == "5":
            print("-------------")
            print("Wynik =", a ** b)
            print("-------------")
        else:
            print("-------------")
            print("Nieznane działanie")
            print("-------------")

    if opcja1 == 2:
        import random

        print("------ ZGADNIJ LICZBĘ ------")

        start = input("Wpisz START aby zacząć: ").lower()
        if start != "start":
            print("-------------")
            print("Trzeba było wpisać START 😄")
            print("-------------")
            continue

        liczba = random.randint(1, 10)
        proby = 0
        max_proby = 5

        while proby < max_proby:
            odpowiedz = int(input("Zgadnij liczbę (1-10): "))
            proby += 1

            if odpowiedz == liczba:
                print("-------------")
                print("BRAWO! Zgadłeś w", proby, "próbie!")
                print("-------------")
                break
            elif odpowiedz < liczba:
                print("-------------")
                print("Za mało!")
                print("-------------")
            else:
                print("-------------")
                print("Za dużo!")
                print("-------------")

        else:
            print("-------------")
            print("Koniec prób! Liczba to była:", liczba)
            print("-------------")

    if opcja1 == 3:
        print("Aby korzystać ze strony Python.com proszę się zalogować")

        proby = 0
        max_proby = 3

        while proby < max_proby:

            login = input("Proszę wpisać login: ")
            password = input("Proszę wpisać hasło: ")
            proby += 1

            if login == "admin" and password == "1234":
                print("-------------")
                print("Zalogowano pomyślnie!")
                print("-------------")
                break
            else:
                print("-------------")
                print("Błędny login lub hasło")
                print("-------------")

        else:
            print("-------------")
            print("Zablokowaliśmy dostęp do konta z powodu zbyt wielu nieudanych prób")
            print("-------------")

    if opcja1 == 4:
        import random

        print("----SUPER ULTRA RPG----")
        print("-----------------------")

        zycie_gracza = 100
        zycie_wroga = 150

        while True:

            print("1. Atak")
            print("2. Leczenie")
            print("3. Ucieczka")

            wybór = int(input("Proszę wpisać cyfrę odpowiadającej danej opcji: "))

            if wybór == 1:
                obrazenia = random.randint(1, 10)
                obrazenia1 = random.randint(1, 10)
                zycie_wroga -= obrazenia
                zycie_gracza -= obrazenia1
                print("-------------")
                print("Zaatakowałeś Ogra Marcina i zadałeś mu", obrazenia, "HP")
                print("Życie Ogra Marcina:", zycie_wroga)
                print("-------------")
                print("Natomiast Ogr Marcin zadał ci", obrazenia1, "HP")
                print("Twoje życie", zycie_gracza)
                print("-------------")
            elif wybór == 2:
                leczenie = random.randint(5, 15)
                print("-------------")
                print("Uleczyłeś się i zdobyłeś", leczenie, "HP")
                zycie_gracza += leczenie
                if zycie_gracza > 100:
                    zycie_gracza = 100
                print("Twoje życie", zycie_gracza)
                print("-------------")
            elif wybór == 3:
                print("-------------")
                print("Uciekłeś, ale zobaczymy się jescze tak?.")
                break

            if zycie_wroga <= 0:
                print("Gratulacje,WYGRAŁEŚ!")
                break
            if zycie_gracza <= 0:
                print("Ohh,przegrałeś. Może następnym razem się uda.")

                break
    if opcja1 == 5:
        print("---WITAMY W SUPER QUIZIE---")
        print("---------------------------")
        print("---------------------------")
        print("---------------------------")
        kaka = input("--WPISZ START ŻEBY ZACZĄĆ-- ")

        if kaka == "start":
            print("--ZACZYNAJMY!--")
        else:
            print("Miałeś wpisać START!!!")
            exit()

        punkty = 0

        while True:

            print("Pytanie 1.")
            print("W JAKIM JĘZYKU ZROBIONY ZOSTAŁ TEN PROGRAM?")
            print("A) Python           B) Java           C) Unity           D) Lua")
            odp1 = input("A twoja odpowiedz to?: ")

            if odp1 == "A":
                print("-----------")
                print("GRATULACJE!! To była poprawna odpowiedz!")
                print("-----------")
                punkty += 1
            else:
                print("-----------")
                print("Niestety poprawna odpowiedz to odpowiedz A) Python.")
                print("-----------")

            print("Pytanie 2.")
            print("Jak na inmie ma dziadek Lisy oraz Barta simpsonów")
            print("A) Joe          B) Burns           C) Abraham           D) Moe")
            odp2 = input("A twoja odpowiedz to?: ")

            if odp2 == "C":
                print("-----------")
                print("GRATULACJE!! Jest to poprawna odpowiedz")
                print("-----------")
                punkty += 1
            else:
                print("-----------")
                print("Niestety poprawna odpowiedz to odpowiedz C) Abraham.")
                print("-----------")

            print("Pytanie 3.")
            print("Postać 'MARIO' z seri gier Mario Brothers ma brata. Jaki jest jego główny kolor?")
            print("A) Pomarańczowy           B) Zielony           C) Czerwony           D) Niebieski")
            odp3 = input("Jaka jest twoja odpowiedz?: ")

            if odp3 == "B":
                print("-----------")
                print("GRATULACJE!! Jest to poprawna  opowiedz!")
                print("-----------")
                punkty += 1
            else:
                print("-----------")
                print("Niestety poprawna odpowiedz to odpowiedz B) Zielony.")
                print("-----------")

            print("Pytanie 4.")
            print("Gra 'Grand Theft Auto 6' ma zaplanowaną premierę na dzień")
            print(
                "A) 24 Kwietnia 2026r.   B) 1 Listopad 2026r.     C) 15 Stycznia 2027r.      D) 19 Listopada 2026r.")
            odp4 = input("Jaka jest twoja odpowiedz?: ")

            if odp4 == "D":
                print("-----------")
                print("GRATULACJE!! Jest to poprawna odpowiedz!")
                print("-----------")
                punkty += 1
            else:
                print("-----------")
                print("Niestety poprawna odpowiedz to D) 19 Listopada 2026r.")
                print("-----------")

            print("Gratulacje doszedłeś/aś do końca a twój wynik końcowy to", punkty, "punkty. Gratulacje!")
            break

    if opcja1 == 6:
        print("-------------")
        print("Oczywiście, żegnam.")

        break
