with open("czwartydzien2020.txt","r") as f:
    wszystko=f.read()
    paszporty=[]
    print(wszystko)
    for item in wszystko:
        paszport=[]
        paszport=wszystko.split("\n\n")
paszporty.append(paszport)
print(paszporty)
dane2=[]
for item in paszporty:
    for dane in item:
        dane1=dane.split("\n")
        dane2.append(dane1)
dane3=[]
for itm in dane2:
    for t in itm:
        slowa=t.split()
        dane3.append(slowa)
print(dane2)
