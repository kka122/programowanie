
with open("drugidzien2021.txt", "r") as f:
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
