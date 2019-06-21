with open('pogoda.txt') as f:
    dane = f.readlines()

# print(dane)

tablica_danych = []

nrl = 0

for el in dane:
    if nrl > 0:
        # el - na wejściu '75;10,5;2;C;4\n'.split(sep=';')
        d_1linia = el.split(sep=';')
        # dostaję splitowane elementy w tablicy ['75', '10,5', '2', 'C', '4\n']
        # print(d_1linia)
        lp = int(d_1linia[0])
        temp = float(d_1linia[1].replace(',', '.'))
        opad = int(d_1linia[2])
        kchm = d_1linia[3]
        wchm = d_1linia[4].strip('\n') # ucina końcowy znak \n
        pojed_dzien = [lp, temp,opad, kchm, wchm]
        tablica_danych.append(pojed_dzien)

    nrl += 1

# print(tablica_danych)

tab_ciag = []
tab_mciag = []
old_temp = 0

for dzien in tablica_danych:
    akt_temp = dzien[1]
    if akt_temp > old_temp:
        tab_mciag.append(dzien)
    else:
        tab_ciag.append(tab_mciag)
        tab_mciag = []
    old_temp = akt_temp
            
print(tab_ciag)


max_dl =0
for elem in tab_ciag:
    dl = len(elem)
    if dl > max_dl:
        max_ciag = elem[:]
        max_dl = dl
    
print('total:',max_ciag)
print('==============================',len(max_ciag))
print('pierwszy dzień',max_ciag[0][0],'ostatni dzień', max_ciag[-1][0])
