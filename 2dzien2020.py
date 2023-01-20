with open("drugidzien2020.txt","r") as f:
    wszystko=f.read().split("\n")
    dane = []
    for i in wszystko:
        item=i.split()
        dane.append(item)
    print(dane)
    print("to tego momentu jest g")
    gotowe_dane=[]
    for itm in dane:
        for ite in itm:
            item1=ite.replace("-"," ")
            item2=item1.replace(":"," ")
            gotowe_dane.append(item2)
    print(gotowe_dane)

