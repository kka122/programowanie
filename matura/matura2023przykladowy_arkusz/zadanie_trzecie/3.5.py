with open("liczby_przyklad.txt.txt","r") as f:
    wszystko=f.read().split("\n")
ilosc_par=0
def ilosc_trojek(M,A,B ):
    for i in range(0, M):
        if (A**i)%M==B:
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