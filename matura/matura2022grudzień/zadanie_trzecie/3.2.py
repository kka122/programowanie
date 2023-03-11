def czy_liczba_jest_pierwsza(k):
    for j in range(2, k):
        if k % j == 0:
            return False
    return 1

with open("liczby_przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
liczby_pierwsze=0

for i in wszystko:
    k=int(i)-1
    if czy_liczba_jest_pierwsza(k)==1:
        liczby_pierwsze+=1

print(liczby_pierwsze)