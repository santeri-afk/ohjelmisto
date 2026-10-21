lentoaseman = {"EFHK":"Helsinki-Vantaa", 
               "EFOU":"Oulu", 
               "EFRO":"Rovaniemi", 
               "EFTU":"Turku"}

print("komennot: ")
print("luo")
print("hae")
print("lopeta")

komento = input("Anna komento haluatko syöttää luoda uuden lentoaseman, hakea tai lopettaa ohjelman: ")

lopeta = "lopeta"


while komento != lopeta:
    if komento == "luo":
        icao = input("Anna uuden luomasi lentoaseman ICAO koodi: ")
        nimi = input("Anna uuden luomasi lentoaseman nimi: ")
        
        if icao in lentoaseman or nimi in lentoaseman:
            print(f"lentoaseman {nimi} on jo lisätty")

        else:
            lentoaseman[icao] = nimi
            print(f"lentoaseman {nimi} onnistuneesti luotu")

    elif komento == "hae":
        haku = input("Anna hakemasi lentoaseman ICAO koodi: ")
        if haku in lentoaseman:
            lentoasemannimi = lentoaseman[haku]
            print(f"Hakemasi lentoaseman nimi on {lentoasemannimi}")

        else:
            print("lentoasemaa ei löytynyt antamallasi koodilla")

    else:
        print("komentoa ei tunnisteta")
        print("komennot ovat: ")
        print("luo")
        print("hae")
        print("lopeta")


    komento = input("Anna komento haluatko syöttää luoda uuden lentoaseman, hakea tai lopettaa ohjelman: ")
