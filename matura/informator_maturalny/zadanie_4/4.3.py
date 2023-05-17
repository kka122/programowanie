def wczytanie_pliku():
    with open("dane4.txt","r")as f:
        wszystko=f.read().split("\n")
    return wszystko




def main():
    liczby=wczytanie_pliku()
    for i in range(len(liczby)):
        for j in range(len(liczby)):
            if int(liczby[i])>int(liczby[j]) and j!=i and i>j:



main()