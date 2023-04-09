with open("dzien_pierwszy","r") as f:
    wszystko=f.read().split(",")
zbior_dobrych_komend=[]
for komendy in wszystko:
    dobre_komendy=komendy.replace(" ", "")
    zbior_dobrych_komend.append(dobre_komendy)
print(zbior_dobrych_komend)
