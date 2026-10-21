class inventaario:
    def __init__(self):
        self.tavarat = ["miekka", "kilpi"]

    def lisaa_tavara(self, tavara):
        self.tavarat.append(tavara)

    def tulosta_tavarat(self):
        for tavara in self.tavarat:
            print(tavara)


pelaaja = inventaario()


pelaaja.lisaa_tavara("Juomapullo")
pelaaja.tulosta_tavarat()

