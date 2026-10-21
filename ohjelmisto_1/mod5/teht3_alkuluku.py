
alkuluku = int(input("Anna luku: "))
a = False

for i in range(2, alkuluku):
    if alkuluku % i == 0:
        print("tämä ei ole alkuluku")
        a = True
        break


if a == False:
    print("luku on alkuluku")

    
   
       

