with open("dzien_drugi") as f:
    wszystko=f.read().split("\n")
najwieksza_wartosc_linijki=0
najmniejsza_wartosc_linijki=0
wynik=0
roznice_wartosci_linijki=[]
nowe_linijki=[]
for i in wszystko:
    liczby=i.split()
    linijki_liczb=[]
    for liczba in liczby:
        liczb=int(liczba)
        linijki_liczb.append(liczb)
    nowe_linijki.append(linijki_liczb)
print(nowe_linijki)

ilorazy=[]
for linijki in nowe_linijki:
    for liczby1 in linijki:
        for liczby in linijki:
            if liczby % liczby1==0 and liczby!=liczby1:
                iloraz = int(liczby/liczby1)
                ilorazy.append(iloraz)
            else:
                pass
print(sum(ilorazy))