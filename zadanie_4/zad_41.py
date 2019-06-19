import math

plik = 'przyklad.txt'

def potega_3(liczba):
    lp3 = False
    wykl = 0
    while lp3 == False:
        wyn_pot = 3 ** wykl
        if wyn_pot > liczba:
            return False, wykl
        if wyn_pot == liczba:
            return True, wykl
        wykl += 1

def log_pot3(liczba):
    wynik = math.log(liczba,3)
    ok = wynik.is_integer()
    return True if ok else False 

def log_pot32(liczba):
    return True if math.log(liczba,3).is_integer() else False 

def log_pot33(liczba):
    wynik = math.log(liczba,3)
    ok = wynik.is_integer()
    if ok==True:
        return True
    else:
        return False 


with open(plik) as f:
    dane = f.readlines()

#print(dane)
tablica_danych = []

for elem in dane:
    tablica_danych.append(int(elem))

print(tablica_danych)

poteg_3 = 0

for elem in tablica_danych:
    wyn = log_pot32(elem)
    if wyn:
        print('test:',elem)
        poteg_3 += 1

print('Znalazlem:',poteg_3)
