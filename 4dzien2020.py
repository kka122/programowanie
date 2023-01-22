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


def is_passport_valid(passport):
    if passport.get("byr") is  None:
        return False
    if passport.get("iyr") is  None:
        return False
    if passport.get("eyr") is  None:
        return False
    if passport.get("hgt") is  None:
        return False
    if passport.get("hcl") is  None:
        return False
    if passport.get("ecl") is  None:
        return False
    if passport.get("pid") is  None:
        return False
    return True

count3=0
for passport in slowniki:
    if is_passport_valid(passport) == True:
        count3+=1


print(count3)