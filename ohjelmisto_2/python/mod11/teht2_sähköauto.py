import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetin):
        self.akku = akkukapasiteetin
        super().__init__(rekisteritunnus, huippunopeus)
    def tulosta_tiedot(self):
        print(f"sähköauto kulki {self.kuljettu_matka}")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin):
        self.tankki = bensatankin
        super().__init__(rekisteritunnus, huippunopeus)
    def tulosta_tiedot(self):
        print(f"bensa auto kulki {self.kuljettu_matka}")


autot = []
autot.append(Sähköauto("ABC-15",180,52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))
tunti = 0
while tunti < 3:
    for auto in autot:
            muutos = random.randint(5, 15)
            auto.kiihdytä(muutos)
            auto.kulje()
            tunti += 1

for t in autot:
    t.tulosta_tiedot()