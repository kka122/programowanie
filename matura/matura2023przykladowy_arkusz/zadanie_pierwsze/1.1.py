with open("szachy_przyklad.txt","r") as f:
    wszystko=f.read().split("\n\n")
    plansze=[]
for plansza in wszystko:
    linijki=plansza.split("\n")
    plansze.append(linijki)

liczba_pustych_kolumn=0
for plansza in plansze:
    print(" ")
    kolumna_2=[]
    for wiersz in plansza:
        kolumna_2.append(wiersz[2])
    print(kolumna_2)
    if kolumna_2.count(".")==8:
        liczba_pustych_kolumn+=1
print(liczba_pustych_kolumn)
plansza=plansze[2]
wiersz=plansza[1]
literka=wiersz[2]
print(literka)


literka=plansze[2][1][2]
print(literka)


count=0
plansza=plansze[1]
plansza_2=plansze[2]
wiersz_1=plansza[1]
wiersz_2=plansza_2[1]
print(wiersz_1.count("."))



