with open("pary.txt","r")as f:
    wszystko=f.read()
dobre_pary=[]
linijka=wszystko.split("\n")
for i in linijka:
    para_liczb=i.split()
    N=100_000
    wywolane_liczby=[]
    def rysuj(x):
        wywolane_liczby.append(x)
        if 2*x<=N:
            rysuj(2*x)
        if (2*x)+1<=N:
            rysuj((2*x)+1)


    rysuj(int(para_liczb[0]))
    if int(para_liczb[-1]) in wywolane_liczby:
        print(para_liczb)
