kanta = 0
korkeus = 0
piiri = 0 
pinta_ala = 0

kanta = int(input("Anna suorakulmion kanta: "))
korkeus = int(input("Anna suorakulmion korkeus: "))

piiri = (2 * (kanta + korkeus))
pinta_ala = (korkeus * kanta)

print(f"suorakulmion piiri on: {piiri}")
print(f"suorakulmion pinta ala on: {pinta_ala}")