with open('/home/abix/matura-inf-2019-rozszerzona/zadanie_4/przyklad.txt') as f:
    dane = f.readlines()

for elem in dane:
	print(elem)
	x = int(elem)
	type(x)
	print(x*2)
