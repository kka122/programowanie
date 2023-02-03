with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
print(wszystko)
liczba_liter=[]
for i in wszystko:
    dane=i.split(" ")
    if dane[0]== "DOPISZ":
        liczba_liter.append(dane[-1])
    elif dane[0]== "USUN":
        liczba_liter.remove(liczba_liter[-1])
    elif dane[0]== "ZMIEN":
        liczba_liter.remove(liczba_liter[-1])
        liczba_liter.append(dane[1])
    elif dane[0]== "PRZESUN":
        litera=chr(ord(dane[1])+1)
        liczba_liter.remove(dane[1])
        liczba_liter.insert(liczba_liter.index(dane[1]),litera)
        if dane[-1]== "Z":
            liczba_liter.remove(dane[1])
            liczba_liter.insert(liczba_liter.index(dane[1]),chr(ord(dane[1])-26))

print(liczba_liter)