def wczytanie_pliku():
    with open("dane3.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko

def main():
    wszystko=wczytanie_pliku()
    przedzialy=[]
    for item in wszystko:
        dlugosc_przedzialow = []
        k=1
        przedzial=item.split()
        for i in range(int(przedzial[0]),int(przedzial[-1])):
            dlugosc_przedzialow.append(i)
        przedzialy.append(dlugosc_przedzialow)
    print(przedzialy)




main()
