def get_input():
    with open("dzien_trzeci", "r") as f:
        plecaki=f.read().split("\n")
    return plecaki

def wspolny_element_plecakow(plecak1,plecak2,plecak3):
    return set(plecak1)&set(plecak2)&set(plecak3)

def litera_na_liczbe(litera):
    if litera ==litera.upper():
        return ord(litera)-65+27
    elif litera ==litera.lower():
        return ord(litera)-64-32


def main():
    plecaki=get_input()
    i=3
    grupy=[]
    suma=0
    while i<=len(plecaki):
        grupy.append(plecaki[i-3:i])
        i+=3
    for grupa in grupy:
        litera=wspolny_element_plecakow(grupa[0],grupa[1],grupa[2])
        lista_liter=list(litera)
        suma+=litera_na_liczbe(lista_liter[0])
    print(suma)

main()







