pituus = float(input("Anna teidän pituus: "))
ikä = int(input("anna ikäsi: "))

if pituus >= 140 and ikä < 7:
    print("saat mennä aikuisten laiteissiin paitsi tulirekeen pitää olla 8 vuotias")

elif pituus >= 140 and pituus < 195:
    print("saat mennä aikuisten laiteissiin")

elif pituus > 100 and pituus < 140:
    print("saat mennä lasten laiteissiin")

elif pituus >= 195:
        print("pääset kaikkii laitteisiin paitsi kirnuun missä on all 195cm raja")
