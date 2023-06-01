with open("mecz_przyklad.txt","r")as f:
    wszystko=f.read()
ilosc_a=[]
ilosc_b=[]
count_a=0
count_b=0
for i in wszystko:
    if i=="A":
        count_a+=1
        ilosc_a.append(count_a)
        count_b=0
    else:
        count_b+=1
        ilosc_b.append(count_b)
        count_a=0


dobre_passy_a=0
ilosc_max_a=max(ilosc_a)
ilosc_max_b=max(ilosc_b)
dobre_passy_b=0
for item in ilosc_a:
    if item==10:
        dobre_passy_a+=1
for item2 in ilosc_b:
    if item2==10:
        dobre_passy_b+=1
print("najdluzsza passa a",ilosc_max_a,"ilosc dobrych pass a",dobre_passy_a)
print("najdluzsza passa b",ilosc_max_b,"ilosc dobrych pass b",dobre_passy_b)
print("najdluzsza passa jest dla litery A i jest to ",ilosc_max_a,"ilosc dobrych pass",dobre_passy_a+dobre_passy_b)