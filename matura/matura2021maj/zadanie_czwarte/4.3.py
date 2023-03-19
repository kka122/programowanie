with open("instrukcje.txt", "r") as f:
    linijki=f.read().split("\n")
    print(linijki)
    litery=[]
count=0
ilosc_liter={}
for item in linijki:
    dane=item.split(" ")
    print(dane)
    if dane[0]=="DOPISZ":
        litery.append(dane[-1])
for litera in litery:
    value=litery.count(litera)
    key=str(litera)
    ilosc_liter[value]=key
print(ilosc_liter)
maksymalna_wartosc=max(ilosc_liter.keys())
print(maksymalna_wartosc)
szukana_litera=ilosc_liter[37]
print(szukana_litera)

