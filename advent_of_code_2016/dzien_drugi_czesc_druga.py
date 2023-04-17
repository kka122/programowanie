keypad=[["1"],["2","3","4"],["5","6","7","8","9"],["A","B","C"],["D"]]
with open("dzien_drugi","r") as f:
    wszystko=f.read().split()
wiersze=1
kolumny=1
punkt_poczatkowy=keypad[wiersze][kolumny]
haslo=[]
for komendy in wszystko:
    for komenda in komendy:
        if komenda=="L":
            if wiersze == 0:
                wiersze=wiersze
            if wiersze==1:
                wiersze-=1
        elif komenda=="U":
            if  kolumny ==0:
                kolumny=kolumny
            if kolumny ==1 or kolumny==2 or kolumny==3 or kolumny==4:
                kolumny-=1
        elif komenda=="D":
            if kolumny ==4:
                kolumny=kolumny
            if kolumny==0 or kolumny==1 or kolumny==2 or kolumny==3:
                kolumny+=1
        elif komenda=="R":
            if wiersze ==4:
                wiersze = wiersze
            if wiersze==0 or wiersze==1 or wiersze==2 or wiersze==3:
                wiersze+=1
    print(keypad[wiersze][kolumny])

print(haslo)