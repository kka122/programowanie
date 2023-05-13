def get_input():
    with open("dzien_trzeci", "r") as f:
        plecaki=f.read().split("\n")
    return plecaki

def dzielenie_plecaka(plecak):
    p = int(len(plecak) / 2)
    przedzial1=plecak[:p]
    przedzial2=plecak[p:]
    return przedzial1,przedzial2

def wspolny_element_przedzialow(przedzial1,przedzial2):
    return set(przedzial1)&set(przedzial2)

def litera_na_liczbe(litera):
    if litera ==litera.upper():
        return ord(litera)-65+27
    elif litera ==litera.lower():
        return ord(litera)-64-32

def main():
    plecaki=get_input()
    liczba=0
    for plecak in plecaki:
        przedzial1,przedzial2=dzielenie_plecaka(plecak)
        litery=wspolny_element_przedzialow(przedzial1,przedzial2)
        for litera in litery:
            liczba+=litera_na_liczbe(litera)
    print(liczba)


main()







