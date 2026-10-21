
vuodenajat = ("kevät", "kesä", "Syksy", "Talvi")


kuukausi = input("Anna kuukautesi numerona: ")

while kuukausi != "":
    kuukausi = int(kuukausi)
    if kuukausi >= 3 and kuukausi <=5:
        print("On Kevät")
        kuukausi = input("Anna kuukautesi numerona: ")

    elif kuukausi >= 6 and kuukausi <=8:
        print("On Kesä")
        kuukausi = input("Anna kuukautesi numerona: ")

    elif kuukausi >= 9 and kuukausi <=11:
        print("On Syksy")
        kuukausi = input("Anna kuukautesi numerona: ")

    elif kuukausi >= 1 and kuukausi <= 2 or kuukausi == 12:
        print("On Talvi")
        kuukausi = input("Anna kuukautesi numerona: ")

    else:
        print("Tämä ei ole minkään kuukauden järjestys luku")
        kuukausi = input("Anna kuukautesi numerona: ")