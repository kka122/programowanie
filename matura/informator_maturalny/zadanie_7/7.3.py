with open("szyfrogram.txt","r")as f:
    szyfr=f.read().split("\n")
with open("czestosc.txt","r") as r:
    dekodowanie=r.read().split("\n")
szyfr_rozdzielony=[]
szyfr_w_liczbach=[]
slownik_dekodujacy={}
for i in szyfr:
    for k in i:
        szyfr_rozdzielony.append(k)
with open("czestosc.txt","r") as r:
    dekodowanie=r.read().split("\n")
for d in dekodowanie:
    wartosci_liczbowie=d.split()
    slownik_dekodujacy[wartosci_liczbowie[0]]=wartosci_liczbowie[-1]

for litera in szyfr_rozdzielony:
    szyfr_w_liczbach.append(slownik_dekodujacy[litera])
print(szyfr_w_liczbach)
