with open("drugidzien2021.txt", "r") as f:
    wszystko = f.read()
    wiersze = wszystko.split("\n")
    print(wiersze)
    aim=0
    glebokosc=0
    odleglosc=0
    for item in wiersze:
        komend = item.split(" ")
        if komend[0]== "forward":
            odleglosc+=int(komend[1])
            kierunek=int(komend[1])*aim
        elif komend[0] == "down":
            glebokosc+=int(komend[1])
            aim+=int(komend[1])
        elif komend[0] == "up":
            glebokosc-=int(komend[1])
            aim-=int(komend[1])

print(glebokosc*odleglosc)
print("Część druga")
with open("drugidzien2021.txt", "r") as f:
    wszystko = f.read()
    wiersze = wszystko.split("\n")
    print(wiersze)
    aim=0
    glebokosc=0
    odleglosc=0
    for item in wiersze:
        komend = item.split(" ")
        if komend[0]== "forward":
            odleglosc+=int(komend[1])
            glebokosc+=int(komend[1])*aim
        elif komend[0] == "down":
            aim+=int(komend[1])
        elif komend[0] == "up":
            aim-=int(komend[1])

print(glebokosc*odleglosc)