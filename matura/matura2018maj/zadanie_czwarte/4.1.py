with open("sygnaly.txt", "r") as f:
    wszystko = f.read()
    slowa = []
    count = 0
for item in wszystko:
    slowo=wszystko.split("\n")

slowa.append(slowo[39::40])
print(slowa)
haslo=[]
for slowo1 in slowa:
    for slowo2 in slowo1:
        haslo.append(slowo2[9])
print(haslo)
print("nastepna czesc")

