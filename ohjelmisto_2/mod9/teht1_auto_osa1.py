class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka


auto = Auto("ABC-123", 142)

print(f"auton rekiesteri on: {auto.rekisteritunnus}")
print(f"Huippunopeus on {auto.huippunopeus} km/h")
print(f"auton tämän hetkinen nopeus {auto.tämänhetkinen_nopeus} km/h")
print(f"Auton kuljettu matka {auto.kuljettu_matka}")