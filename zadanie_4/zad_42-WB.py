# zadanie 4.2
def silnia_rek(n):
    """Obliczanie silni rekurencyjnie"""
    if n>1:
        return n*silnia_rek(n-1)
    elif n in (0,1):
        return 1


print(silnia_rek(7))
