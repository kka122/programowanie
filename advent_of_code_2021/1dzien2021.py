
with open("pierwszydzien2021.txt", "r") as f:
    wszystko1 = f.read()
    wszystko2=wszystko1.split("\n")
    wszystko = []
    wszystko.append(wszystko2)
    print(wszystko)
    count=0
    liczby=[]
    for item in wszystko:
        for itm in item:
            i = int(itm)
            liczby.append(i)
    for liczb in range(1,len(liczby)):
        if liczby[liczb] > liczby[liczb - 1]:
            count+=1
print(count)
print("czesc druga")
with open("pierwszydzien2021.txt", "r") as f:
    wszystko1 = f.read()
    wszystko2=wszystko1.split("\n")
    wszystko = []
    wszystko.append(wszystko2)
    print(wszystko)
    count=0
    liczby=[]
    for item in wszystko:
        for itm in item:
            i = int(itm)
            liczby.append(i)
    suma_liczb=[]
    for liczb in range(1,len(liczby)):
        suma=liczby[liczb]+liczby[liczb-1]+liczby[liczb-2]
        suma_liczb.append(suma)
    count1=0
    for suma1 in range(1, len(suma_liczb)):
        if suma_liczb[suma1] > suma_liczb[suma1 - 1]:
            count1 += 1
print(count1)