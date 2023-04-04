with open("szostydzien2020.txt", "r") as f:
    wszystko=f.read().split("\n\n")
    print(wszystko)
    odpowiedzi1=[]
    for item in wszystko:
        odpowiedzi=item.replace("\n","")
        odpowiedzi1.append(odpowiedzi)
    print(odpowiedzi1)
    zbiory=[]
    for item1 in odpowiedzi1:
            zbiory.append(set(item1))
    print(zbiory)
    count=0
    for ite in zbiory:
        for itm in ite:
            count+=1
    print(count)
    print("druga czesc")
with open("szostydzien2020.txt", "r") as f:
    wszystko=f.read().split("\n\n")
print(wszystko)
odpowiedzi1 = []
grupy=[]

for item in wszystko:
    odpowiedzi=item.split("\n")
    osoby=[]
    for it in odpowiedzi:
        zbior=set(it)
        osoby.append(zbior)
    grupy.append(osoby)
dlugosc=0
for grupa in grupy:
    obecnaosoba=grupa[0]
    for osoba in grupa:
        obecnaosoba=obecnaosoba&osoba
    print(obecnaosoba)
    dlugosc+=len(obecnaosoba)
print(dlugosc)
