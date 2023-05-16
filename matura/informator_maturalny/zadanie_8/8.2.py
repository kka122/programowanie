def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko




def sprawdzanie_par(ciag):
    for i in range(0,len(ciag)):
        for k in range(0,len(ciag)):
            if ciag[i]>ciag[k] and i<k:
                return True

def main():
    licznik = 0
    ciag=wczytanie_pliku()
    for i in ciag:
        for k in ciag:
            if ciag.index(i)<ciag.index(k):
                if int(i)>int(k):
                    licznik+=1
                    print(licznik)




main()