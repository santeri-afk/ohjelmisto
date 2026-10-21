def lukujen_summa(luvut):
    summa = 0 
    for i in luvut:
        summa += i
    return summa




kokonailuku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lukujen_summa(kokonailuku)
print("listan kokonais summa on:",lukujen_summa(kokonailuku))