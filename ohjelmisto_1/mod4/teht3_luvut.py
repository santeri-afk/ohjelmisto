luku = input("Anna luku: ")
suurin_luku = int(luku)
pienin_luku = int(luku)
loppu = ""
while luku != loppu:

    muunto = int(luku)
    if muunto > suurin_luku:
        suurin_luku = muunto
        

    elif muunto < pienin_luku:
        pienin_luku = muunto

    luku = input("Anna luku: ")
    

print(f"pieninin luku on {pienin_luku}")
print(f"Suurin luku on {suurin_luku}")



