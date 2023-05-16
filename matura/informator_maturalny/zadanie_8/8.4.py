def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko