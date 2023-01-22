with open("czwartydzien2020.txt","r") as f:
    wszystko=f.read()
    paszporty=[]
    print(wszystko)
    for item in wszystko:

        paszport=wszystko.split("\n\n")
paszporty.append(paszport)
print(paszporty)
dane2=[]
for item in paszporty:
    for dane in item:
        dane1=dane.replace("\n"," ")
        dane2.append(dane1)
slowniki=[]
count=0
count2=0
for it in dane2:
    atrybuty=it.split()
    slownik={}
    for atrybut in atrybuty:
        atrybut1=atrybut.split(":")
        key=atrybut1[0]
        value=atrybut1[1]
        slownik[key]=value
    slowniki.append(slownik)
for key in slowniki:
    for itm in key:
        if key[itm] == "byr" and key[itm] =="iyr" and key[itm] =="eyr" and key[itm] == "hgt" and key[itm] =="hcl" and key[itm]== "ecl" and key[itm] == "pid":
            count+=1

print(slowniki)
print(count)