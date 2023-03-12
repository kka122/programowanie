with open("liczby_przyklad.txt","r") as f:
    wszystko=f.read().split("\n")
ilosc_liczb_pierwszych=0
def czy_liczba_jest_pierwsza(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return 1
for item in wszystko:
    liczby=item.split()
    liczba_M=int(liczby[0])
    if czy_liczba_jest_pierwsza(liczba_M)==1:
        ilosc_liczb_pierwszych+=1
print(ilosc_liczb_pierwszych)