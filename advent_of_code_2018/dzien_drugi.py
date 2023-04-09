with open("dzien_drugi","r")as f:
    wszystko=f.read().split("\n")
powtarza_sie_dwa_razy=0
powtarza_sie_trzy_razy=0
lista_ilosci_ile_razy_powtarza_sie_litera=[]
for slowo in wszystko:
    ilosc_ile_razy_powtarza_sie_litera = []
    for litera in slowo:
        ilosc_ile_razy_powtarza_sie_litera.append(slowo.count(litera))
    lista_ilosci_ile_razy_powtarza_sie_litera.append(ilosc_ile_razy_powtarza_sie_litera)
for i in lista_ilosci_ile_razy_powtarza_sie_litera:
    zbiory=set(i)
    for liczba in zbiory:
        if liczba == 2:
            powtarza_sie_dwa_razy+=1
        elif liczba==3:
            powtarza_sie_trzy_razy+=1
print(powtarza_sie_trzy_razy*powtarza_sie_dwa_razy)