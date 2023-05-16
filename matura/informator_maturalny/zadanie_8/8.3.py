def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko


def sprawdzanie_liczb_wiekszych_od_poprzedniej(terazniejsza,poprzednia):
    if (int(terazniejsza)<int(poprzednia)):
        return True

def sprawdzanie_najdluzszego_ciagu(liczba_luk_nieparzystych):
    liczenie_dlugosci_najdluzszego_wyrazu=0
    dlugosc_najdluzszego_wyrazu=[]
    for i in liczba_luk_nieparzystych:
        if i==1:
            liczenie_dlugosci_najdluzszego_wyrazu+=1
        if i==0:
            dlugosc_najdluzszego_wyrazu.append(liczenie_dlugosci_najdluzszego_wyrazu)
            liczenie_dlugosci_najdluzszego_wyrazu=0
    print(max(dlugosc_najdluzszego_wyrazu)+1)



def main():
    ciag=wczytanie_pliku()
    liczba_luk_nieparzystych = []

    for i in range(len(ciag)-1):

        if sprawdzanie_liczb_wiekszych_od_poprzedniej(ciag[i],ciag[i+1])==True:
            liczba_luk_nieparzystych.append(1)
        else:
            liczba_luk_nieparzystych.append(0)

    print(liczba_luk_nieparzystych)
    sprawdzanie_najdluzszego_ciagu(liczba_luk_nieparzystych)




main()