keypad=[["X","X","X","X","X","X","X"],["X","X","X","1","X","X","X"],["X","X","2","3","4","X","X"],["X","5","6","7","8","9","X"],["X","X","A","B","C","X","X"],["X","X","X","D","X","X","X"],["X","X","X","X","X","X","X"]]
with open("dzien_drugi","r") as f:
    wszystko=f.read().split("\n")
wiersze=3
kolumny=1
punkt_poczatkowy=keypad[wiersze][kolumny]
haslo=[]
for komendy in wszystko:
    for komenda in komendy:
        if komenda=="U":
            wiersze-=1
            if keypad[wiersze][kolumny]=="X":
                wiersze+=1
        elif komenda=="R":
            kolumny+=1
            if keypad[wiersze][kolumny]=="X":
                kolumny-=1
        elif komenda=="L":
            kolumny-=1
            if keypad[wiersze][kolumny]=="X":
                kolumny+=1
        elif komenda=="D":
            wiersze+=1
            if keypad[wiersze][kolumny]=="X":
                wiersze-=1
    print(keypad[wiersze][kolumny])


