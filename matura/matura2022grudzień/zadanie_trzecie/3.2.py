with open("liczby_przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
liczby_pierwsze=0
for i in wszystko:
    k=int(i)-1
    for g in range(2,k-1):
        if k%g==0:
            print("liczba nie jest pierwsza")
            liczby_pierwsze+=1
print(liczby_pierwsze)
