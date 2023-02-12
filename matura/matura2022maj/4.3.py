with open("przyklad.txt","r")as f:
    wszystko=f.read().split("\n")
print(wszystko)
for i in wszystko:
    print()