with open("pary.txt","r")as f:
    wszystko=f.read()
dobre_pary=[]
linijka=wszystko.split("\n")
for i in linijka:
    para_liczb=i.split()
    if int(para_liczb[0])*2==int(para_liczb[-1]):
        dobre_pary.append(para_liczb)
    elif (int(para_liczb[0])*2)+1==int(para_liczb[-1]):
        dobre_pary.append(para_liczb)
print(dobre_pary)