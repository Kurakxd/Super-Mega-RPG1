#Są dwa typy funkcji
def dodwanieReturn(licza1, liczba2):
    wynik = licza1+liczba2
    return wynik

def monozenie(licza1, liczba2):
    wynik = licza1*liczba2
    return wynik

wynik_dodwania= dodwanieReturn(1,6)
print(wynik_dodwania)

wynik_mnozenia = monozenie(1,6)
print(wynik_mnozenia)


# to zwróci none - czyli brak wartości
def dodawanieVoid(licza1, liczba2):
    wynik = licza1+liczba2

#Funkcja może zwrócic też dwa argumenty
def info_o_userz(imie, nazwisko, rok_urodzenia):
    wiek = 2026 - rok_urodzenia;
    pierwsza_litera_imie = imie[0]
    pierwsza_litera_nazwisko = nazwisko[0]
    return pierwsza_litera_imie, pierwsza_litera_nazwisko, wiek

dane = info_o_userz("Marek", "Jastrz", 1985)
print("dane")
print(dane)

print("Dane ale z indeksami")
print(dane[0])
print(dane[1])
print(dane[2])


print("Print a,b,c pojedynczo")
imie,naz,rok = info_o_userz("Marek", "Jastrz", 1985)
print("imie:" + imie)
print("naz:" + naz)
print("rok" + str(rok))



# tutaj będzie błąd bo nie można dodać liczy i Nono
wynik_void = dodawanieVoid(4, 5)
dodawanie_voida = dodwanieReturn(wynik_mnozenia, wynik_void)
print(dodawanie_voida)



