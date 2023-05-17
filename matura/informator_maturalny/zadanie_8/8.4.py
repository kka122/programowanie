def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko


def tworzenie_ciagow(ciag):
    stworzone_nowe_ciagi=[]
    for i in range((len(ciag)-1)):
        pojedynczy_ciag=[]
        if ciag[i+1]>ciag[i]:
            pojedynczy_ciag.append(ciag[i])
            pojedynczy_ciag.append(ciag[i+1])
        stworzone_nowe_ciagi.append(pojedynczy_ciag)
    return stworzone_nowe_ciagi
def sumowanie_ciagow(nowe_male_ciagi):
    nowy_duzy_ciag=[]
    for i in nowe_male_ciagi:
        for k in i:
            nowy_duzy_ciag.append(k)
    return nowy_duzy_ciag

def tworzenie_duzego_ciagu(ciag):
    duzy_ciag=[]
    for i in range((len(set(ciag))-1)):
        if int(ciag[i])<int(ciag[i+1]):
            duzy_ciag.append(ciag[i])
    print(duzy_ciag)


def usuwanie_nieptrzebnych_elementow(ciag):
    poprawny_ciag=[]
    for i in range(1,len(ciag)):
        if ciag[i-1]!=ciag[i]:
            poprawny_ciag.append(ciag[i-1])
    poprawny_ciag.append(ciag[-1])
    return poprawny_ciag
def main():
    ciag=wczytanie_pliku()
    d=tworzenie_ciagow(ciag)
    o=sumowanie_ciagow(d)
    print(o)
    k=usuwanie_nieptrzebnych_elementow(o)
    tworzenie_duzego_ciagu(k)

main()