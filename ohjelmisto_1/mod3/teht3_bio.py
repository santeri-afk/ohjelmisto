
sukupuoli = input("Anna biologisen sukupuolesi mies tai nainen: ")
sukupuolilower = sukupuoli.lower()

if sukupuolilower == "mies":
    hemoglobiiniarvon = int(input("Anna hemoglobiiniarvosi: "))

    if hemoglobiiniarvon >= 134 and hemoglobiiniarvon <= 195 :
        print("hemoglobiiniarvosi on normaali")

    elif hemoglobiiniarvon < 134:
        print("hemoglobiiniarvosi on liian alhainen")

    elif hemoglobiiniarvon > 195:
        print("hemoglobiiniarvosi on liian korkea")


if sukupuolilower == "nainen":
    hemoglobiiniarvon = int(input("Anna hemoglobiiniarvosi: "))
    if hemoglobiiniarvon >= 117 and hemoglobiiniarvon <= 175 :
        print("hemoglobiiniarvosi on normaali")

    elif hemoglobiiniarvon < 117:
        print("hemoglobiiniarvosi on liian alhainen")

    elif hemoglobiiniarvon > 175 :
        print("hemoglobiiniarvosi on liian korkea")


        