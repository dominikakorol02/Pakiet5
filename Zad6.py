#Zad6

def zaczyna_sie_na_a(slowo):
    return slowo.startswith('a')

lista_slow = ['arbuz', 'banan', 'pomarańcza', 'ananas', 'jabłko']

slowa_na_a = list(filter(zaczyna_sie_na_a, lista_slow))
print("Słowa zaczynające się na 'a':", slowa_na_a)

liczby = [1, 2, 3, 4, 5]

kwadraty_liczb = list(map(lambda x: x**2, liczby))
print("Kwadraty liczb:", kwadraty_liczb)
