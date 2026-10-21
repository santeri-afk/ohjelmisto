import math

luvut = []
laskuri = 0
print("Anna kolme kokonais lukua:")

while laskuri < 3:
    luku = int(input("Anna kokonais luku: "))
    laskuri += 1
    luvut.append(luku)

summa = sum(luvut) 
tulo = math.prod(luvut)
keskiarvo = sum(luvut) / len(luvut) # jakaa lukujen summan lukujen määrällä


print(f"Summa: {summa}")
print(f"tulo: {tulo}")
print(f"keskiarvo: {keskiarvo:6.2f}")


#luku1 = int(input("Anna kokonais luku: "))
#luku2 = int(input("Anna kokonais luku: "))
#luku3 = int(input("Anna kokonais luku: "))
  
#summa = (luku1 + luku2 + luku3)
#tulo = (luku1 * luku2 * luku3)
#keskiarvo = (summa / summa)

