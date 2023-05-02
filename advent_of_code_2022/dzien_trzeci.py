with open("dzien_trzeci","r")as f:
    plecaki=f.read().split("\n")
plecak_podzielony=[]
podzielony_przedzial=[]
litery=[]
wlasciwe_litery=[]
for plecak in plecaki:
    p=int(len(plecak)/2)
    przedzial1=plecak[:p]
    przedzial2=plecak[p:]
    for litera in przedzial1:
        for litera1 in przedzial2:
            if litera==litera1:
                litery.append(litera1)
p=0
dobre_litery=set(litery)
for i in dobre_litery:

    if i ==i.upper():
        p+=ord(i)-65+27

    elif i ==i.lower():
        p+=ord(i)-64-32
print(p)



