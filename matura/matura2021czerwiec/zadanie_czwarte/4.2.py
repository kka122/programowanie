def wczytanie_pliku():
    with open("przyklad.txt","r")as f:
        wszystko=f.read().split("\n")
    return wszystko


def szukanie_hasla(linie):
    haslo=""
    k=0
    for i in linie:
        for linie in i:
            haslo+=linie[k]
            k+=1
    return haslo


def main():
    wszystkie_linie=wczytanie_pliku()
    potrzebne_linie=[]
    potrzebne_linie.append(wszystkie_linie[19::20])
    print(potrzebne_linie)
    print(szukanie_hasla(potrzebne_linie))

main()