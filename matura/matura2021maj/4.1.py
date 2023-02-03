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
print(len(liczba_liter))
