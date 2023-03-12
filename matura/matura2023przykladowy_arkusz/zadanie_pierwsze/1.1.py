with open("szachy_przyklad.txt","r") as f:
    wszystko=f.read().split("\n\n")
for plansza in wszystko:
    linijka=plansza.split("\n")
    for miejsce in plansza:
        