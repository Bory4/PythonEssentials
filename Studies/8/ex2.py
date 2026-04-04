#!/usr/bin/python
def suma_liczb(nazwa_pliku):
    try:
         return sum([int(linia) for linia in open(nazwa_pliku, "r").read().strip().split("\n")])
    except Exception as e:
        print(e)
        exit()

print(suma_liczb("plik"))
