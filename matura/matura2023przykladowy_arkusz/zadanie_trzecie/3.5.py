with open("liczby_przyklad.txt","r") as f:
    wszystko=f.read().split("\n")
ilosc_par=0
def ilosc_trojek(x,y,z):
    for i in range(0, x-1):
        if y**i%x==z:
            return True
    return False
for item in wszystko:
    liczby=item.split()
    liczba_M=int(liczby[0])
    liczba_a=int(liczby[1])
    liczba_b=int(liczby[-1])
    if ilosc_trojek(liczba_M,liczba_a,liczba_b)==True:
        ilosc_par+=1



print(ilosc_par)