litra = 0
def bensa(määrä):
        muutos = määrä * 3.786
        return muutos

while True:
    gallons = int(input("Anna bensan määrä: "))
    litraa = bensa(gallons)
    if gallons < 0:
        break
    else:
        print(f"{gallons} gallonaa on {litraa:.2f} litraa.")





4