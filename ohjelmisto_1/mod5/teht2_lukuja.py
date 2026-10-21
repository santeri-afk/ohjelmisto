luku = input("Anna luku: ")
luvut = []
loppu = ""

while luku != loppu:
    X = int(luku)
    luvut.append(X)
    luku = input("Anna luku: ")

luvut.sort(reverse=True)
print(luvut[0:5])
    


