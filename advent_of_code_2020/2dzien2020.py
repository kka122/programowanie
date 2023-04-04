with open("drugidzien2020.txt", "r") as f:
    wszystko=f.read().split("\n")
    dane = []
    for i in wszystko:
        item=i.split()
        dane.append(item)
    print(dane)
    print("to tego momentu jest g")
    gotowe_dane=[]
    count=0
    jd=[]
    for itm in dane:
        print(itm)
        zakres = itm[0]
        litera = itm[1]
        haslo = itm[2]
        zakres1=zakres.split("-")
        litera1=litera.replace(":","")
        liczba_liter=haslo.count(litera1)
        print(liczba_liter)
        print(zakres1[-1])
        if liczba_liter >= int(zakres1[0]) and liczba_liter <= int(zakres1[-1]):
            count+=1
print(count)
with open("drugidzien2020.txt", "r") as f:
    wszystko=f.read().split("\n")
    dane = []
    for i in wszystko:
        item=i.split()
        dane.append(item)
    print(dane)
    print("to tego momentu jest g")
    gotowe_dane=[]
    count1=0
    jd=[]
    for itm in dane:
        zakres = itm[0]
        litera = itm[1]
        haslo = itm[2]
        zakres1=zakres.split("-")
        litera1=litera.replace(":","")
        if haslo[int(zakres1[0])-1] == litera1 or haslo[int(zakres1[-1])-1] == litera1:
            count1+=1
        if haslo[int(zakres1[0])-1] == litera1 and haslo[int(zakres1[-1])-1] == litera1:
            count1-=1
print(count1)