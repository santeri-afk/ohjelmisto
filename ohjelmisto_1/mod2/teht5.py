
leiviskät = float(input("Anna leiviskät. "))
print(leiviskät)

naula = float(input("Anna naulat. "))
print(naula)

luoti = float(input("Anna luodit. "))
print(luoti)

luodin_paino = float(13.3 * naula)
naulan_paino = float(425.6 * naula)
leiviskät_paino = float(8512 * leiviskät)



grammat = (luodin_paino + naulan_paino + leiviskät_paino)
kilot = grammat // 1000
loput =  grammat % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot}kilogrammaa ja {loput:0.2f}grammaa ")