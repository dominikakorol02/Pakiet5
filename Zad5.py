#Zad5

def liczby_parzyste(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wynik_parzyste = liczby_parzyste(liczby)
print("Liczby parzyste:", wynik_parzyste)

pole_prostokata = lambda a, b: a * b

bok_a = 4
bok_b = 6
wynik_pola = pole_prostokata(bok_a, bok_b)
print("Pole prostokąta:", wynik_pola)
