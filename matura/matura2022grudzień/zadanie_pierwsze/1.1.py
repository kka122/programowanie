with open("mecz_przyklad.txt", "r") as f:
    wszystko=f.read()
pierwsza=wszystko[0]
count=0
for i in wszystko:
    if pierwsza!=i:
        count+=1
    pierwsza=i
print(count)