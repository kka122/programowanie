with open("mecz_przyklad.txt", "r") as f:
    wszystko=f.read()
count=0
for i in range(1,len(wszystko)):
    litera=wszystko[i]
    poprzednia=wszystko[i-1]
    if poprzednia!=litera:
        count+=1
    pierwsza=i
print(count)