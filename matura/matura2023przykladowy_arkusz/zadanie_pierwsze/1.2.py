with open("szachy_przyklad.txt","r")as f:
    wszystko=f.read().split("\n\n")
liczba_plansz_w_rownowadze=0
liczba_bierek_na_planszach=[]
for plansza in wszystko:
    ilosc_czarnych_figur=0
    ilosc_bialych_figur=0
    znaki_z_planszy=plansza.replace("\n","")
    for znak in znaki_z_planszy:
        if znak.isupper()==True:
            ilosc_bialych_figur+=1
        if znak.islower()==True:
            ilosc_czarnych_figur+=1
    if ilosc_bialych_figur==ilosc_czarnych_figur:
        liczba_plansz_w_rownowadze+=1
        ilosc_bierek_lacznie=ilosc_czarnych_figur+ilosc_bialych_figur
        liczba_bierek_na_planszach.append(ilosc_bierek_lacznie)

print(liczba_plansz_w_rownowadze)
print(min(liczba_bierek_na_planszach))