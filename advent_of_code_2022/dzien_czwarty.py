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

pary2=[]
for i in pary1:
    pary3=[]
    for k in i:
        zakresy1=[]
        for j in range(int(k[0]),int(k[1])+1):
            zakresy1.append(str(j))
        pary3.append(zakresy1)
    pary2.append(pary3)

dluzszy_zakres=[]
dobre_pary=0
for item in pary2:
    if len(item[0])>len(item[-1]):
        dluzszy_zakres.append(len(item[0]))
    else:
        dluzszy_zakres.append(len(item[-1]))

suma_zakresow=[]
for l in pary2:
    suma_zakresow.append(set(l[0]+l[-1]))

for k in range(0,len(dluzszy_zakres)):
    if dluzszy_zakres[k]==len(suma_zakresow[k]):
        dobre_pary+=1
print(dobre_pary)
