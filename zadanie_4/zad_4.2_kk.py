# zadanie 4.2
print('test zadania 4.2')

def silnia_rek(n):
    """Obliczanie silni rekurencyjnie"""
    if n>1:
        return n*silnia_rek(n-1)
    elif n in (0,1):
        return 1

def licz_silnie_liter(elem):
    calk_silnia = 0
    for znak in elem:
        sil_znaku = silnia_rek(int(znak))
        calk_silnia += sil_znaku
    return calk_silnia

with open('liczby.txt') as f:
    dane = f.readlines()

tablica_danych = []

for elem in dane:
    tablica_danych.append(int(elem))

print('tablica przed:',len(dane))
print('tablica po:',len(tablica_danych))

wyniki_dobre = []

for elem in tablica_danych:
    wart_silni = licz_silnie_liter(str(elem))
    if elem == wart_silni:
        print('Liczba:',elem)
        wyniki_dobre.append('Wynik '+str(elem)+'\n')

with open('przyklad-odpowedz.txt','w') as f:
    f.writelines(wyniki_dobre)
