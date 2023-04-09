with open("dzien_czwarty","r") as f:
    wszystko=f.read().split("\n")

pary1=[]
for pary in wszystko:
    elf=pary.split(",")
    zakresy=[]
    for zakres in elf:
        liczba=zakres.split("-")
        zakresy.append(liczba)
    pary1.append(zakresy)
print(pary1)
pary2=[]
for i in pary1:
    zakresy1=[]
    for k in i:
        for j in range(int(k[0]),int(k[1])+1):
            zakresy1.append(j)
        print(zakresy1)
