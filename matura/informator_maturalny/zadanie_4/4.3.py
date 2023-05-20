def wczytanie_pliku():
    with open("dane4.txt","r")as f:
        wszystko=f.read().split("\n")
    return wszystko




def main():
    liczby=wczytanie_pliku()
    j=0
    l=0
    roznice=[]
    wszystkie_roznice=[]
    for k in range(len(liczby)):
        for i in range(len(liczby)):
            if liczby[i]!=liczby[k]:
                j=i-k
                l=int(liczby[i]) - int(liczby[k])
                roznice.append(j)
                wszystkie_roznice.append(l)
        # wszystkie_roznice.append(roznice)
    print(max(roznice))



main()