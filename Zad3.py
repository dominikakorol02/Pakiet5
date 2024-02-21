#Zad3

total = 0
def dodaj_do_total(liczba):
    global total
    total += liczba

def pomnoz_przez_lokalna(liczba):
    local_variable = 2
    wynik = liczba * local_variable
    print("Wynik mnożenia przez zmienną lokalną:", wynik)

dodaj_do_total(5)
dodaj_do_total(10)
print("Wartość zmiennej globalnej total po dodawaniu:", total)

pomnoz_przez_lokalna(3)
