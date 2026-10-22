import random
class Auto:
    def __init__(self, rekisteritunnus = 0, huippunopeus = 0, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

        return

    def kulje(self):
        self.kuljettu_matka = self.kuljettu_matka + self.tämänhetkinen_nopeus 

    def pelaajat(self, määrä):
        racers = []
        for i in range(1, määrä):
            maksimi_nopeus = random.randint(100, 200)
            i = Auto(f"ABC-{i}", maksimi_nopeus)
            racers.append(i)
        return racers
            
           
Winner = False
kilpailijat = Auto.pelaajat("", 11)
while Winner != True:

    for auto in kilpailijat:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje()
    for i in kilpailijat:
        if i.kuljettu_matka >= 10000:
            Winner = True
            break

print("rekisteritunnus | huippunopeus | tämänhetkinen_nopeus | kuljettu_matka")
for a in kilpailijat:
    if a.kuljettu_matka >= 10000:
        print(f"{a.rekisteritunnus} | {a.huippunopeus} | {a.tämänhetkinen_nopeus} | {a.kuljettu_matka} | Voittaja" + " |")
        print(f"-----------------------------------------")

    else:
        print(f"{a.rekisteritunnus} | {a.huippunopeus} | {a.tämänhetkinen_nopeus} | {a.kuljettu_matka}" + " |")
        print(f"-----------------------------------------")





