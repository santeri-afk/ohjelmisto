import random

N = int(input("Anna pisteiden määrä: "))
n = 0
laskuri = 0

while laskuri < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    laskuri += 1
    if x ** 2 + y ** 2 < 1:
        n = n + 1

pi = (4*n/N)

print(f"pi likiarvo on {pi}")

