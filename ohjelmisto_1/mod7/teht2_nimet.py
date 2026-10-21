#https://fi.wikibooks.org/wiki/Python_3/Joukko


nimet = set()

nimi = input("Anna nimi: ")

while nimi != "":

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimi = input("Anna nimi: ")

    else:
        print("Uusi nimi")
        nimet.add(nimi)
        nimi = input("Anna nimi: ")


for i in nimet:
    print(i)

