def wczytanie_pliku():
    with open("dane3.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko

def main():
    wszystko=wczytanie_pliku()
    dlugosc_przedzialow=[]
    for item in wszystko:
        k=1
        przedzialy=item.split()
        for i in range(int(przedzialy[0]),int(przedzialy[-1])):
           k+=1
        dlugosc_przedzialow.append(k)
    print(sorted(dlugosc_przedzialow)[0],sorted(dlugosc_przedzialow)[1])




main()

