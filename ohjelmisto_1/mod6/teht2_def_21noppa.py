import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maksimisilmäluku: "))

while True:
    silmaluku = noppa(maksimi)
    print(f"heitit {silmaluku}")

    if silmaluku == maksimi:
        break
