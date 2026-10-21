class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = 143

        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

        return

    def kulje(self, kulje):
        self.kuljettu_matka = self.tämänhetkinen_nopeus * kulje

        

auto = Auto("ABC-123", 142,)

auto.kiihdytä(60)
print(f"Auton nopeus: {auto.tämänhetkinen_nopeus}")
print(f"kuljettu matka: {auto.kuljettu_matka}")
auto.kulje(1.5)
print(f"kuljettu matka: {auto.kuljettu_matka}")


