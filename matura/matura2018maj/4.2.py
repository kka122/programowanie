with open("sygnaly.txt","r")as f:
    wszystko=f.read().split("\n")
liczba_liter=[]
for i in wszystko:
    liczba_liter.append(len(i))
print(max(liczba_liter))
liczba_roznych_liter=[]
slownik={}
for i in wszystko:
    liczba_roznych_liter.append(len(set(i)))
    slownik[len(set(i))]=i
    if len(set(i))==26:
        print(slownik[26])
print(max(liczba_roznych_liter))
print("szukane slowo to SUOLDQWISCDRFLRWHZBNTMIAPHALMNCWHVGMXOZSQNXWXSFELZVTUTILXWKCTYBQYSUAKNYJKRXDJQYHXAQGWN i ilosc roznych liter to 26")

