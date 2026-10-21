hyttiluokka = input("Anna hyttisi luokka: ")
uppercase_text = hyttiluokka.upper()

if uppercase_text == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")

elif uppercase_text == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif uppercase_text == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif uppercase_text == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")