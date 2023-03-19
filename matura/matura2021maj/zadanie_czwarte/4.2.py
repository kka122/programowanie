with open("przyklad.txt", "r")as f:
    wszystko=f.read().split("\n")
for i in wszystko:
    dane=i.split(" ")
    if dane[0] == "DOPISZ":


