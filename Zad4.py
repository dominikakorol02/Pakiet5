#Zad4

def dodaj(a, b):
    return a + b

def pomnoz(a, b):
    return a * b

def wykonaj_operacje_na_liczbach(x, y, funkcja_operacji):
    wynik = funkcja_operacji(x, y)
    print("Wynik operacji:", wynik)

wykonaj_operacje_na_liczbach(3, 5, dodaj)

wykonaj_operacje_na_liczbach(4, 6, pomnoz)
