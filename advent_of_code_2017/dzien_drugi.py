with open("dzien_drugi") as f:
    wszystko=f.read().split("\n")
najwieksza_wartosc_linijki=0
najmniejsza_wartosc_linijki=0
wynik=0
roznice_wartosci_linijki=[]
for i in wszystko:
    liczby=i.split()
    linijki_liczb=[]
    for liczba in liczby:
        liczb=int(liczba)
        linijki_liczb.append(liczb)
    najwieksza_wartosc_linijki = max(linijki_liczb)
    najmniejsza_wartosc_linijki = min(linijki_liczb)
    wynik = najwieksza_wartosc_linijki-najmniejsza_wartosc_linijki
    roznice_wartosci_linijki.append(wynik)
print(sum(roznice_wartosci_linijki))

