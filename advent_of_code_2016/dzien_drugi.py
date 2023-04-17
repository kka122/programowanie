keypad=[["1","2","3"],["4","5","6"],["7","8","9"]]
with open("dzien_drugi","r") as f:
    wszystko=f.read().split()
wiersze=1
kolumny=1
punkt_poczatkowy=keypad[wiersze][kolumny]
haslo=[]
for komendy in wszystko:
    for komenda in komendy:
        if komenda=="U":
            if wiersze == 0:
                wiersze=wiersze
            if wiersze==1 or wiersze ==2:
                wiersze-=1
        elif komenda=="L":
            if  kolumny ==0:
                kolumny=kolumny
            if kolumny ==1 or wiersze==2:
                kolumny-=1
        elif komenda=="R":
            if kolumny ==2:
                kolumny=kolumny
            if kolumny==0 or kolumny==1:
                kolumny+=1
        elif komenda=="D":
            if wiersze ==2:
                wiersze = wiersze
            if wiersze==0 or wiersze==1 :
                wiersze+=1
        print(keypad[wiersze][kolumny])
print(haslo)