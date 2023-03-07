with open("liczby_przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
liczby=[]
liczby_pierwsze=[]
for i in wszystko:
    liczba=int(i)-1
    liczby.append(liczba)
for item in liczby:
    for i in range(2,item-1):
        if item%i==0:
            print("nie jest podzielna")
        else:
            liczby_pierwsze.append(item)
print(liczby_pierwsze,len(liczby_pierwsze))
