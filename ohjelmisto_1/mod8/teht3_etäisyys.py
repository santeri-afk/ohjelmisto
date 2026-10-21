import mysql.connector
from geopy import distance

def lentokentien_matka(kenttä1, kenttä2):
    laskuri = 1
    sql =f"Select latitude_deg, longitude_deg from airport where ident='{kenttä1}' or ident='{kenttä2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print("hakemallassi lentokentillä on näin kaukana toisistaan")
        for kursori in tulos:
            
            if laskuri == 1:
                a = kursori
                laskuri += 1
            elif laskuri == 2:
                b = kursori
                dist = distance.distance(a, b).km
                dist_rounded = round(dist, 2)
                print(f"{dist_rounded} km")






yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    #en laita salasanaa näkyvillä koska se on public reposity
    password="******",
    autocommit=True
    )

print("Anna kaksi maata niin lasken matkan niiten välillä")
lentokenttä1 = input("Anna ensimmäisen lentokentän icao koodi: ")
lentokenttä2 = input("Anna toisen lentokentän icao koodi: ")
lentokentien_matka(lentokenttä1, lentokenttä2)