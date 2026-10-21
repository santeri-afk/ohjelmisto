import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
        self.racers = []

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = 143

        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

        return

    def kulje(self, kulje):
        self.kuljettu_matka = self.tämänhetkinen_nopeus * kulje

    def pelaajat(self, määrä):
        for i in range(0, määrä):
            maksimi_nopeus = random.randint(100, 200)
            auto = Auto(f"ABC-{i}", maksimi_nopeus)

            
           
Winner = False
while Winner != True:

    






