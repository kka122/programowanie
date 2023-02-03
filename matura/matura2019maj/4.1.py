with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
n=0
lista_liczb=[]
for liczby in wszystko:
    liczba=int(liczby)
