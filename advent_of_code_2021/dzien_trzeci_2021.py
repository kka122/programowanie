with open("dzien_trzeci_2021.txt", "r") as f:
    wszystko=f.read().split("\n")
gamma=[]
epsilon=[]
for i in  range(len(wszystko[0])):
    kolumna=[]
    for liczba in wszystko:
        kolumna.append(liczba[i])
    if kolumna.count("1")>kolumna.count("0"):
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")

tekst_epsilon=""
tekst_gamma=""
for cyfra in epsilon:
    tekst_epsilon+=cyfra
for cyfra in gamma:
    tekst_gamma += cyfra
liczba_epsilon=int(tekst_epsilon,2)
liczba_gamma=int(tekst_gamma,2)
print(liczba_epsilon*liczba_gamma)


