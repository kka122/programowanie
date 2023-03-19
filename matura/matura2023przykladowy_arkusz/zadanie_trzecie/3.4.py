with open("liczby.txt","r") as f:
    wszystko=f.read().split("\n")
ilosc_par=0
from math import gcd
def czy_liczba_jest_pierwsza(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return 1
for item in wszystko:
    liczby=item.split()
    liczba_M=int(liczby[0])
    liczba_a=int(liczby[1])
    nwd=gcd(liczba_M,liczba_a)
    if nwd ==1:
        ilosc_par+=1
print(ilosc_par)