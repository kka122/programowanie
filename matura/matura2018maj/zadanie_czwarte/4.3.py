with open("sygnaly.txt", "r")as f:
    wszystko=f.read().split("\n")
dobre_slowa = []
for i in wszystko:
    wartosc=[]
    for letter in i:
        wartosc.append(ord(letter))
    if max(wartosc)-min(wartosc) <= 10:
        dobre_slowa.append(i)
for slowo in dobre_slowa:
    print(slowo)

