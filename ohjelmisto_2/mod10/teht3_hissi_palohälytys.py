class Hissi:
    def __init__(self, ylin=10, alin=-2, hissin_numero=0):
        self.ylin_kerros = ylin
        self.alin_kerros = alin 
        self.kerros = alin
        self.hissin_numero = hissin_numero

    def siirry_kerrokseen(self, kohdekerros):
        while kohdekerros != self.kerros:
            
            while kohdekerros < self.kerros:
                self.kerros_alas(1)
           
            while kohdekerros > self.kerros:
                self.kerros_ylös(1)


    def kerros_ylös(self, siirtymä_ylös):
        self.kerros += siirtymä_ylös
        print(f"Hissi {self.hissin_numero} on {self.kerros} kerroksessa")

    def kerros_alas(self, siirtymä_alas):
        self.kerros -= siirtymä_alas
        print(f"Hissi {self.hissin_numero} on {self.kerros} kerroksessa")
        


class Talo:
    def __init__(self, ylin, alin, hissi):
        self.hissit = []
        self.alin = alin

        for i in range(hissi):
            uusi_hissi = Hissi(ylin, alin, i)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)



    def palo_hälytys(self):
        for i in range(len(self.hissit)):
            self.aja_hissiä(i, self.alin)
            
            


talo = Talo(10, 1, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)

talo.palo_hälytys()

