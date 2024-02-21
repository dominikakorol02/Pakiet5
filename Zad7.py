#Zad7

def podnies_do_kwadratu(x):
    return x ** 2

def dodaj_piec(x):
    return x + 5

def zastosuj_funkcje(do_zastosowania, wartosc):
    for funkcja in do_zastosowania:
        wartosc = funkcja(wartosc)
    return wartosc

lista_funkcji = [podnies_do_kwadratu, dodaj_piec]

liczba = float(input("Podaj liczbę: "))

wynik = zastosuj_funkcje(lista_funkcji, liczba)
print("Wynik:", wynik)
