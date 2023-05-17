def wczytanie_pliku():
    with open("dane3.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko
def liczenie(dlugosci_przedzialow):
    j=[]
    for i in dlugosci_przedzialow:
        j.append(dlugosci_przedzialow.count(i))
    return j





def main():
    wszystko=wczytanie_pliku()
    dlugosc_przedzialow=[]
    for item in wszystko:
        k=1
        przedzialy=item.split()
        for i in range(int(przedzialy[0]),int(przedzialy[-1])):
           k+=1
        dlugosc_przedzialow.append(k)
    ilosc_tych_samych_licz=liczenie(dlugosc_przedzialow)
    print(ilosc_tych_samych_licz)
    ds=[]
    for i in range(len(ilosc_tych_samych_licz)):
        s=[]
        s.append(ilosc_tych_samych_licz[i])
        s.append(dlugosc_przedzialow[i])
        ds.append(s)
    print(max(ds))




main()