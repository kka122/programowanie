with open("mecz_przyklad.txt", "r") as f:
    wszystko=f.read()
liczba_meczy=wszystko.count("AB")+wszystko.count("BA")
print(liczba_meczy)