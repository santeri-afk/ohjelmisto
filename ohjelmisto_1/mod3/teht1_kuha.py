kuha = float(input("laita tähän kalan pituus senttimetreinä: "))

if kuha < 37:
    puuttuu = 37 - kuha
    print(f"kalan alimmasta pyyntimitasta puuttuu {puuttuu:0.2f} senttimetriä")
    print("kuha liian pieni laske takaisin veteen ")

else:
    print("kuha tarpeeksi iso")