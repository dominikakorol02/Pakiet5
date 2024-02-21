#Zad9

from functools import reduce

def znajdz_najwieksza(liczby):
    return reduce(lambda x, y: x if x > y else y, liczby)

lista_liczb = [7, 12, 4, 18, 9, 22, 5, 26]

najwieksza_liczba = znajdz_najwieksza(lista_liczb)
print("Największa liczba:", najwieksza_liczba)


def oblicz_sume(x, y):
    return x + y

lista_liczb = [7, 12, 4, 18, 9, 22, 5, 26]

suma = reduce(oblicz_sume, lista_liczb)
srednia = suma / len(lista_liczb) if len(lista_liczb) > 0 else None

print("Średnia:", srednia)
