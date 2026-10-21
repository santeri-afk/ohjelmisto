

class Inventaario:
    def __init__(self):
        self.tavarat = []

    def lisaa_tavara(self, tavara):
        self.tavarat.append(tavara)

    def tulosta_tavarat(self):
        print("Inventaario:")
        for tavara in self.tavarat:
            print(tavara)


# Luodaan inventaario
inventaario = Inventaario()

# Lisätään tavaroita
inventaario.lisaa_tavara("Miekka")
inventaario.lisaa_tavara("Kilpi")
inventaario.lisaa_tavara("Juomapullo")

# Tulostetaan tavarat
inventaario.tulosta_tavarat()
