with open("szachy_przyklad.txt","r") as f:
    wszystko=f.read().split("\n\n")
    plansze=[]
for plansza in wszystko:
    linijki=plansza.split("\n")
    plansze.append(linijki)

liczba_pustych_kolumn=0
for plansza in plansze:
    print(" ")

    for wiersz in plansza:
        kolumna_2=[]
        for i in range(len(wiersz)):
            kolumna_2.append(wiersz[i])
    print(kolumna_2)
    if kolumna_2.count(".")==8:
        liczba_pustych_kolumn+=1
print(liczba_pustych_kolumn)
plansza=plansze[2]
wiersz=plansza[1]
literka=wiersz[2]
print(literka)