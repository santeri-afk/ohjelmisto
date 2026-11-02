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
        for i in range(1, määrä + 1):
            maksimi_nopeus = random.randint(100, 200)
            i = Auto(f"ABC-{i}", maksimi_nopeus)
            racers.append(i)
        return racers

class Kilpailu:
    def __init__(self, nimi, pituus, autot=[]):
        self.autot = autot
        self.kilpailu_nimi = nimi
        self.kilpailun_pituus = pituus

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje()

    def tulosta_tilanne(self):
        print("rekisteritunnus | huippunopeus | tämänhetkinen_nopeus | kuljettu_matka")
        for a in self.autot:
            if a.kuljettu_matka >= self.kilpailun_pituus:
                print(f"{a.rekisteritunnus} | {a.huippunopeus} | {a.tämänhetkinen_nopeus} | {a.kuljettu_matka} | Voittaja" + " |")
                print(f"-----------------------------------------")

            else:
                print(f"{a.rekisteritunnus} | {a.huippunopeus} | {a.tämänhetkinen_nopeus} | {a.kuljettu_matka}" + " |")
                print(f"-----------------------------------------")

    def kilpailu_ohi(self):
        for a in self.autot:
            if a.kuljettu_matka >= self.kilpailun_pituus:
                return True
        return False


kilpailu = Kilpailu("Suuriromuralli", 8000, Auto.pelaajat("", 10))
tunti = 0

i = kilpailu.kilpailu_ohi()

while i != True:
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0 and not tunti == 1:
        kilpailu.tulosta_tilanne()
        kilpailu.kilpailu_ohi() 

    i = kilpailu.kilpailu_ohi()


kilpailu.tulosta_tilanne()

