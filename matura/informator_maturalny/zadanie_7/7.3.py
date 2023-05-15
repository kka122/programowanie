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
klucz={'A': 41, 'B': 42, 'C': 98, 'D': 7, 'E': 18, 'F': 43, 'G': 0, 'H': 36, 'I': 17, 'J': 32, 'K': 91, 'L': 34, 'M': 86, 'N': 39, 'O': 50, 'P': 44, 'Q': 0, 'R': 31, 'S': 0, 'T': 60, 'U': 38, 'V': 16, 'W': 2, 'X': 92, 'Y': 68, 'Z': 15}

for litera in szyfr_rozdzielony:
    szyfr_w_liczbach.append(klucz[litera])
print(szyfr_w_liczbach)
