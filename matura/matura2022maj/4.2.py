with open("liczby.txt","r")as f:
    wszystko=f.read().split("\n")
print(wszystko)
ilosc_czynnikow=[]
def czynnik(num):
    if num == 1:
        return [1]
    n = 2
    czynniki = []
    while n**2 <= num:
        if num % n ==0:
            czynniki.append(n)
            num //= n
        else:
            n+=1
    if num >1:
        czynniki.append(num)
    return czynniki
for itm in wszystko:
    num=int(itm)
    ilosc_czynnikow.append(czynnik(num))
print(ilosc_czynnikow)
dlugosc=[]
najwieksza_ilosc_roznych_czynnikow=[]
for i in ilosc_czynnikow:
    ite=set(i)
    najwieksza_ilosc_roznych_czynnikow.append(len(ite))
    if len(ite) ==6:
        print("dla 6",ite)
    if len(i) == 10:
        print("dla 10",i)
    dlugosc.append(len(i))
print(max(dlugosc))
print(max(najwieksza_ilosc_roznych_czynnikow))
print(16*81*77)
print(2**9*41)
print(2**8*3*73)
print("dla 6",2*3*5*7*13*23)
