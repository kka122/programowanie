with open("szachy.txt","r")as f:
    wszystko=f.read().split("\n\n")
liczba_dobrych_plansz = 0
ilosc_pustych_kolumn_w_planszach=[]
for plansza in wszystko:
    wiersze=plansza.split("\n")
    kolumny = []
    liczba_pustych_kolumn=0
    for i in range(8):
        kolumna=[]
        for wiersz in wiersze:
            kolumna.append(wiersz[i])
        kolumny.append(kolumna)
    for kolumna in kolumny:
        if kolumna.count(".")==8:
            liczba_pustych_kolumn+=1
    if liczba_pustych_kolumn>0:
        liczba_dobrych_plansz+=1
    ilosc_pustych_kolumn_w_planszach.append(liczba_pustych_kolumn)
print(max(ilosc_pustych_kolumn_w_planszach))
print(liczba_dobrych_plansz)
