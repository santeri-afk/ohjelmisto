class Julkaisu:
    def __init__(self, nimi):
        self.julkaisun_nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.krjoittaja = kirjoittaja
        self.sivut = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"kirjan nimi {self.julkaisun_nimi} kirjoittaja on {self.krjoittaja} ja sivuja on {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.toimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.julkaisun_nimi} ja päätoimittaja on {self.toimittaja}")


Julkaisut = []
Julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
Julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for i in Julkaisut:
    i.tulosta_tiedot()