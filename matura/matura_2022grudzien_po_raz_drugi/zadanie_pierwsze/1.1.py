def otworzenie_pliku():
    with open("mecz_przyklad.txt","r") as f:
        return f.read()


def main():
    wszystkie_mecze=otworzenie_pliku()
    print(wszystkie_mecze.count("AB")+wszystkie_mecze.count("BA"))

main()