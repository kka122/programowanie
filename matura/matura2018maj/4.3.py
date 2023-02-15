with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
for i in wszystko:
    wartosc=[]
    dobre_slowa=[]
    for letter in i:
        wartosc.append(ord(letter))
    if max(wartosc)-min(wartosc) <= 10:
        wartosc.clear()
        dobre_slowa.append(i)
print(dobre_slowa)

