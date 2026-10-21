import random

kuutio = int(input("Mikä on arpakuutioiden lukumäärä: "))
luvut = []
laskuri = 0
summa = 0
while kuutio != laskuri:
    kuutio = random.randint(1, 6)
    luvut.append(kuutio)
    laskuri += 1

for i in luvut:
    summa += i

print(f"silmälukujen summan {summa}")
