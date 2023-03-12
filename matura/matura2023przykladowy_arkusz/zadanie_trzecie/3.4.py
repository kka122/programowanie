with open("liczby_przyklad.txt","r") as f:
    wszystko=f.read().split("\n")
ilosc_par=0
def czy_liczba_jest_pierwsza(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return 1
for item in wszystko:
    liczby=item.split()
    liczba_M=int(liczby[0])
    liczba_a=int(liczby[1])
def czy_liczba_M_i_a_sa_wzglednie_pierwsze(x,y):
    if x-y<0:
        wieksza_liczba=y
    else:
        wieksza_liczba=x
    for i in range(2,wieksza_liczba):
        if x%i==0 and y%i==0:
            return False
    return 1

if czy_liczba_jest_pierwsza(liczba_M,liczba_a)==1:
    ilosc_par+=1

print(ilosc_par)


