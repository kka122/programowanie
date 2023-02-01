with open("liczby.txt","r")as f:
    wszystko=f.read().split("\n")
lista_liczb=[]
for i in wszystko:
    liczby=str(i)
    if liczby[0] == liczby[-1]:
        lista_liczb.append(liczby)
print(len(lista_liczb))
print(lista_liczb[0])