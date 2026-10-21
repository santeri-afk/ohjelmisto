import random

kolmenumeroinen = []
nelinumeroinen = []

for _ in range(3):
    b = (random.randint(0, 9)) 
    kolmenumeroinen.append(b)


for _ in range(4):
    a = (random.randint(1, 6)) 
    nelinumeroinen.append(a)

print("kolmenumeroisen koodi")
print(kolmenumeroinen)

print(" ")

print("nelinumeroisen koodi")
print(*nelinumeroinen)