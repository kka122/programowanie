with open("dzien_trzeci","r")as f:
    plecaki=f.read().split("\n")
litery=[]

for plecak in plecaki:
    p=int(len(plecak)/2)
    przedzial1=plecak[:p]
    przedzial2=plecak[p:]
    dobre_litery = []
    for litera in przedzial1:
        for litera1 in przedzial2:
            if litera==litera1:
                dobre_litery.append(litera1)
    litery.append(set(dobre_litery))
print(litery)
x=0
for i in litery:
    for k in i:
        if k ==k.upper():
            x+=ord(k)-65+27
        elif k ==k.lower():
            x+=ord(k)-64-32
print(x)



