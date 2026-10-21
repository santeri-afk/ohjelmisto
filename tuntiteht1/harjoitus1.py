korkeus = int(input("anna tornin korkeus: "))

for i in range(1, korkeus + 1):
    väli = " " * (korkeus - i)
    tähti = "*" * (2 * i - 1)
    print(väli + tähti)