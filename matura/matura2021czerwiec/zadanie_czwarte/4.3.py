def wczytanie_pliku():
    with open("przyklad.txt","r")as f:
        wszystko=f.read().split("\n")
    return wszystko
def dodanie_pierwszej_litery_jako_ostatniej(wszystkie_linie):
    nowa_linia=""
    for linia in wszystkie_linie:
        nowa_linia+=linia
        nowa_linia+=linia[0]
        nowa_linia+=" "
    return nowa_linia
def dodawanie_ostatniej_jao_pierwszej(wszystkie_linie):
    nowa_linia1 = ""
    for linia in wszystkie_linie:
        nowa_linia1 += linia[-1]
        nowa_linia1 += linia
        nowa_linia1 += " "
    return nowa_linia1
def tworzenie_nowych_slow(nowe_linie):
    for i in nowe_linie:
        return i.split(" ")[0:-1]
def czy_slowo_jest_pali(slowo):
    lista1=list(slowo)
    lista2=list(slowo)
    lista1.reverse()
    if lista1==lista2:
        return True
    else:
        return False

def main():
    wszystkie_linie=wczytanie_pliku()
    nowe_linie=[]
    nowe_linie_ostatnia_jako_pierwsza=[]
    nowe_linie.append(dodanie_pierwszej_litery_jako_ostatniej(wszystkie_linie))
    nowe_linie_ostatnia_jako_pierwsza.append(dodawanie_ostatniej_jao_pierwszej(wszystkie_linie))
    pierwsza_dodana=tworzenie_nowych_slow(nowe_linie)
    ostatnia_dodana=tworzenie_nowych_slow(nowe_linie_ostatnia_jako_pierwsza)
    for i in range(len(pierwsza_dodana)):
        if czy_slowo_jest_pali(pierwsza_dodana[i])  or czy_slowo_jest_pali(ostatnia_dodana[i]):
            print(wszystkie_linie[i][25],end="")
main()


