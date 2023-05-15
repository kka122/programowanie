


def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko


def sprawdzanie_luk(terazniejsza,poprzednia):
    if (int(terazniejsza)+int(poprzednia))%2==0:
        return True
    elif (int(terazniejsza)+int(poprzednia))%2==1:
        return False



def main():
    ciag=wczytanie_pliku()
    liczba_luk_parzystych=0
    liczba_luk_nieparzystych=0
    for i in range(0,2022):
        if sprawdzanie_luk(ciag[i],ciag[i+1])==True:
            liczba_luk_parzystych+=1
        elif sprawdzanie_luk(ciag[i],ciag[i+1])==False:
            liczba_luk_nieparzystych+=1
    print(liczba_luk_parzystych,liczba_luk_nieparzystych)



main()