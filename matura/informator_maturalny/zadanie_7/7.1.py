with open("szyfrogram.txt","r")as f:
    wszystko=f.read().split("\n")
wszystkie_linie=[]

for i in wszystko:
    for k in i:
        wszystkie_linie.append(k)

print(wszystkie_linie.count("A"),"A")
print(wszystkie_linie.count("B"),"B")
print(wszystkie_linie.count("C"),"C")
print(wszystkie_linie.count("D"),"D")
print(wszystkie_linie.count("E"),"E")
print(wszystkie_linie.count("F"),"F")
print(wszystkie_linie.count("G"),"G")
print(wszystkie_linie.count("H"),"H")
print(wszystkie_linie.count("I"),"I")
print(wszystkie_linie.count("J"),"J")
print(wszystkie_linie.count("K"),"K")
print(wszystkie_linie.count("L"),"L")
print(wszystkie_linie.count("M"),"M")
print(wszystkie_linie.count("N"),"N")
print(wszystkie_linie.count("O"),"O")
print(wszystkie_linie.count("P"),"P")
print(wszystkie_linie.count("R"),"R")
print(wszystkie_linie.count("S"),"S")
print(wszystkie_linie.count("T"),"T")
print(wszystkie_linie.count("U"),"U")
print(wszystkie_linie.count("W"),"W")
print(wszystkie_linie.count("X"),"X")
print(wszystkie_linie.count("Y"),"Y")
print(wszystkie_linie.count("Z"),"Z")