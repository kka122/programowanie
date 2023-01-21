with open("szostydzien2020.txt","r") as f:
    wszystko=f.read().split("\n\n")
    print(wszystko)
    odpowiedzi1=[]
    for item in wszystko:
        odpowiedzi=item.replace("\n","")
        odpowiedzi1.append(odpowiedzi)
    print(odpowiedzi1)
    zbiory=[]
    for item1 in odpowiedzi1:
            zbiory.append(set(item1))
    print(zbiory)
    count=0
    for ite in zbiory:
        for itm in ite:
            count+=1
    print(count)
    print("druga czesc")
with open("szostydzien2020.txt", "r") as f:
    wszystko = f.read().split("\n\n")
    print(wszystko)
    odpowiedzi1 = []
    for item in wszystko:
        odpowiedzi = item.split("\n")
        odpowiedzi1.append(odpowiedzi)
    print(odpowiedzi1)
    odpowiedzi2=[]
    for item2 in odpowiedzi1:
        for item3 in item2:
            wyraz=set(item3)
            odpowiedzi2.append(wyraz)
            print(wyraz)
            wspolne_odpowiedzi=[]
    for odp in range(1,len(odpowiedzi2)):
        suma=odpowiedzi2[odp]&odpowiedzi2[odp-1]
        wspolne_odpowiedzi.append(suma)
    print(wspolne_odpowiedzi)
    dj=[]
    for itm1 in wspolne_odpowiedzi:
        for itm2 in itm1:
            dj.append(itm2)
    dj1=dj
    count2=0
    for itm3 in dj1:
        count2+=1
    print(count2)