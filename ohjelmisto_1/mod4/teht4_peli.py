import random 

vastaus = int(input("Anna numero 1 - 10 välillä: "))
random_luku = random.randint(1, 10)

while vastaus != random_luku:
    if vastaus > random_luku:
        print("Liian suuri arvaus")
        vastaus = int(input("Anna numero 1 - 10 välillä: "))

    elif vastaus < random_luku:
        print("Liian pieni vaustaus")
        vastaus = int(input("Anna numero 1 - 10 välillä: "))

print("Oikein")
