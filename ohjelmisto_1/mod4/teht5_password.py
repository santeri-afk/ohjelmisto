käyttäjätunnus = "Python"
oikea_salasana = "rules"
laskuri = 1

käyttäjä = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

while käyttäjä != käyttäjätunnus or salasana != oikea_salasana:
    print("käyttäjätunnus tai salasana on väärin kokeile uudestaan")
    käyttäjä = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    laskuri += 1

    if laskuri == 5:
        print("Pääsy evätty")
        break

else:
    print("Tervetuloa")