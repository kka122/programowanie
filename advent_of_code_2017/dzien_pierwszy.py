with open("dzien_pierwszy","r")as f:
    wszystko=f.read().split("\n")
liczby=[]
liczba1=0
for i in wszystko:
    for liczba in i:
        liczby.append(liczba)
print(set(liczby))
print(2+3+7+6+4+1+8+9+5)