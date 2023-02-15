with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
n=1
lista_liczb=[]
for liczby in wszystko:
    liczba=int(liczby)
    if liczba==1:
        lista_liczb.append(liczba)
    elif liczba**(1/n) == 3:
        lista_liczb.append(liczba)
    elif liczba **(1/n) != 3:
        n+=1

print(lista_liczb)