with open("przyklad.txt", "r")as f:
    wszy=f.read().split("\n")
print(wszy)
wszystko=[]
for i in wszy:
    wszystko.append(int(i))

for a in wszystko:
    for b in wszystko:
        for c in wszystko:
            if c%b==0 and b%a==0 and c!=b and b!= a:
                print(a,b,c)

wszystko.sort()
print(wszystko)
n = len(wszystko)

for a in wszystko:
    podzielne = [b for b in wszystko if b%a==0]
    if len(podzielne) > 4:
        print(podzielne)