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
    pary3=[]
    for k in i:
        zakresy1=[]
        for j in range(int(k[0]),int(k[1])+1):
            zakresy1.append(str(j))
        print(zakresy1)
        pary3.append(zakresy1)
    pary2.append(pary3)
print(pary2)


dobre_pary=0
for item in pary2:
    if len(item[0])>len(item[-1]):
        z=item[0].append(item[-1])
        x=len(set(z))
        dobre_pary+=1
    elif len(item[0])<len(item[-1]):
        print(item[-1])
        dobre_pary+=1
print(dobre_pary)

