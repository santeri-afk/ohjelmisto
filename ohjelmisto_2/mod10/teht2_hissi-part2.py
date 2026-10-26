class Hissi:
    def __init__(self, ylin=10, alin=-2):
        self.ylin = ylin
        self.alin = alin 
        self.kerros = alin

    def siirry_kerrokseen(self, kohdekerros):
        
        while kohdekerros != self.kerros:
            
            while kohdekerros < self.kerros:
                self.kerros_alas(1)
           
            while kohdekerros > self.kerros:
                self.kerros_ylös(1)


    def kerros_ylös(self, siirtymä_ylös):
        self.kerros += siirtymä_ylös
        print(f"Hissi on {self.kerros} kerroksessa")

    def kerros_alas(self, siirtymä_alas):
        self.kerros -= siirtymä_alas
        print(f"Hissi on {self.kerros} kerroksessa")


class Talo:
    hissit = []
    
    def __init__(self, ylin_kerros, alin_kerros, hissi):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissi = hissi
        

    def aja_hissiä(self, hissin_numero, kohdekerros):



talo = Talo(10, -2, 3)

