with open("przyklad.txt","r")as f:
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

for a in wszystko:
    for b in wszystko:
        for c in wszystko:
            for d in wszystko:
                for e in wszystko:
                    if e%d==0 and d%c==0 and c%b==0 and b%a==0 and e!=d and d!=c and c != b and b!=a:
                        print(a,b,c,d,e)