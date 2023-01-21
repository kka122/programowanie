with open("drugidzien2020.txt","r") as f:
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
        if int(zakres1[0]) >= liczba_liter and liczba_liter <= int(zakres1[-1]):
            count+=1
print(count)
