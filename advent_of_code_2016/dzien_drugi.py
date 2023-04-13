keypad=[["1","2","3"],["4","5","6"],["7","8","9"]]
with open("dzien_drugi","r") as f:
    wszystko=f.read().split()
wiersze=1
kolumny=1
punkt_poczatkowy=keypad[wiersze][kolumny]
for komendy in wszystko:
    for komenda in komendy:
        if komenda=="U" and 1==wiersze:
            wiersze-=1
            print(keypad[wiersze][kolumny])
        if komenda=="L" and kolumny==1:
            kolumny-=1
            print(keypad[wiersze][kolumny])
        if komenda=="R" and kolumny==1:
            kolumny+=1
            print(keypad[wiersze][kolumny])
        if komenda=="D" and wiersze ==1:
            wiersze+=1
            print(keypad[wiersze][kolumny])
