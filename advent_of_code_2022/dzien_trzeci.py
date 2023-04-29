with open("dzien_trzeci","r")as f:
    plecaki=f.read().split("\n")
plecak_podzielony=[]
for plecak in plecaki:
    p=int(len(plecak)/2)
    przedzial1=[]
    for i in range(p):
        przedzial1.append(plecak[p])
print(przedzial1)


