def wczytanie_pliku():
    with open("przyklad.txt","r")as f:
        wszystko=f.read().split("\n")
    return wszystko


def sprawdzanie_lacznej_ilosci_liter(calosc):
    licznik=0
    for i in calosc:
        for item in i:
            if item == "0":
                licznik+=1
            elif item == "1":
                licznik+=1
            elif item == "2":
                licznik+=1
            elif item == "3":
                licznik+=1
            elif item == "4":
                licznik+=1
            elif item == "5":
                licznik+=1
            elif item == "6":
                licznik+=1
            elif item == "7":
                licznik+=1
            elif item == "8":
                licznik+=1
            elif item == "9":
                licznik+=1
    return licznik




def main():
    wszystkie_wiersze=wczytanie_pliku()
    print(sprawdzanie_lacznej_ilosci_liter(wszystkie_wiersze))





main()