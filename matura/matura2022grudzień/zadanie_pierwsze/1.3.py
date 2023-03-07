with open("mecz_przyklad.txt","r")as f:
    wszystko=f.read()
poprzednia=wszystko[0]
dl=0
res=0
max_dl=0
for i in wszystko:
    if i==poprzednia:
        dl+=1
    else:
        dl=1
    if dl==10:
        res+=1
    if dl>max_dl:
        max_dl=dl
        max_d=i
    poprzednia=i
print(res,max_dl,max_d)