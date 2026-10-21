def lukujen_summa(luvut):
    for i in luvut:
        if i % 2 != 0:
            continue
        else:
            karsittu.append(i)
    return 




kokonailuku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = []
lukujen_summa(kokonailuku)
print("listan kokonais summa on:", kokonailuku)
print("karsittjen lista", karsittu)