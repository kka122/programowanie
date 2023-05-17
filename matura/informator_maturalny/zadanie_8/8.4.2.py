# from itertools import combinations,permutations
import itertools
def wczytanie_pliku():
    with open("dane8.txt","r") as f:
        wszystko=f.read().split("\n")
        return wszystko








def main():
    ciag=wczytanie_pliku()
    print(ciag)
    # print(list(combinations(ciag,3)))
    # print(list(permutations(ciag,3)))





main()


print(help(itertools))