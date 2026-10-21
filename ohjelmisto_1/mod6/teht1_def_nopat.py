import random

def nopat():
    noppa_luku = 0

    while noppa_luku != 6:
        noppa_luku = random.randint(1, 6)
        print(f"heitit {noppa_luku}")

    else:
        return

nopat()