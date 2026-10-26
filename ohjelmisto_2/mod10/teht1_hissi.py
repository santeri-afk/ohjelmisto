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





a = Hissi()
a.siirry_kerrokseen(10)
a.siirry_kerrokseen(-2)

