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

# tutaj będzie błąd bo nie można dodać liczy i Nono
wynik_void = dodawanieVoid(4, 5)
dodawanie_voida = dodwanieReturn(wynik_mnozenia, wynik_void)
print(dodawanie_voida)



