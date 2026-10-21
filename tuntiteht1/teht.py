def tulosta_tahtitorni(korkeus):
    """Tulostaa tähtitorni, jonka korkeus on 'korkeus'."""
    if not isinstance(korkeus, int) or korkeus <= 0:
        print("Korkeuden täytyy olla positiivinen kokonaisluku.")
        return
    
    for i in range(1, korkeus + 1):
        # Tulostetaan välilyönnit ja tähdet
        valit = " " * (korkeus - i)
        tahdet = "*" * (2 * i - 1)
        print(valit + tahdet)

try:
    korkeus = int(input("Anna tornin korkeus: "))
    tulosta_tahtitorni(korkeus)
except ValueError:
    print("Virhe: syötä kokonaisluku.")