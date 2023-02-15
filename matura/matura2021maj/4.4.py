with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
print(wszystko)
liczba_liter=[]
for i in wszystko:
    dane=i.split(" ")
    print(dane)
    if dane[0]== "DOPISZ":
        liczba_liter.append(dane[-1])
    elif dane[0]== "USUN":
        liczba_liter.remove(liczba_liter[-1])
    elif dane[0]== "ZMIEN":
        liczba_liter.remove(liczba_liter[-1])
        liczba_liter.append(dane[1])
    elif dane[0]== "PRZESUN" and dane[-1]!= "Z":
        index=liczba_liter.index(dane[1])
        litera=liczba_liter[index]
        nowa_litera=chr(ord(dane[1])+1)
        liczba_liter[index]=nowa_litera
    elif dane[0]== "PRZESUN" and dane[-1]=="Z":
        index = liczba_liter.index(dane[-1])
        litera = liczba_liter[index]
        nowa_litera = chr(ord(dane[-1]) -25)
        liczba_liter[index] = nowa_litera


print(liczba_liter)
