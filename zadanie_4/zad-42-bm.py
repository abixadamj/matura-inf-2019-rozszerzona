# zadanie 4.2
print('test zadanie 4.2')

def silnia_rek(n):
    """Obliczanie silni rekurencyjnie"""
    if n>1:
        return n*silnia_rek(n-1)
    elif n in (0,1):
        return 1

plik = 'przyklad.txt'
with open(plik) as f:
    dane = f.readlines()

#print(dane)
tablica_danych = []

for elem in dane:
    tablica_danych.append(int(elem))
