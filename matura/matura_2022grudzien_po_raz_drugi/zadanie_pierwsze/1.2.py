def otworzenie_pliku():
    with open("mecz_przyklad.txt","r") as f:
        return f.read()




def main():
    licznik_A=0
    licznik_B=0
    wszystkie_mecze=otworzenie_pliku()
    for i in wszystkie_mecze:
        if i =="A":
            licznik_A+=1
            if licznik_A == 1000:
                break
        elif i =="B":
            licznik_B+=1
            if licznik_B==1000:
                break
    print(licznik_A,licznik_B)

main()