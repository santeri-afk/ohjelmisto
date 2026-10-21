import math
def pizza(halkaisia, hinta):
    sade = halkaisia / 2
    pinta_alacm2 = math.pi * sade ** 2
    pinta_alam2 = pinta_alacm2 / 10000
    yksikkohinta = hinta / pinta_alam2
    return yksikkohinta





pizza1_halkaisia = float(input("Anna ensimmäisen pitsan halkaisia: "))
pizza1_hinta = float(input("Anna ensimmäisen pitsan hinta: "))
yksikkohinta1= pizza(pizza1_halkaisia, pizza1_hinta)

pizza2_halkaisia = float(input("Anna ensimmäisen pitsan halkaisia: "))
pizza2_hinta = float(input("Anna ensimmäisen pitsan hinta: "))
yksikkohinta2 = pizza(pizza2_halkaisia, pizza2_hinta)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pitsa antaa parremin vastinetta hintaa vastaa")

elif yksikkohinta2 < yksikkohinta1:
    print("toka pitsa antaa parremin vastinetta hintaa vastaa")

else:
    print("mollemmat pitsat ovat yhtä hyviä hinnaltaan")