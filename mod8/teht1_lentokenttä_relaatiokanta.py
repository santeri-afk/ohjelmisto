import mysql.connector
def hakee_lentoaseman_icao(icao):   
    sql =f"SELECT name, municipality from airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for kursori in tulos:
            print("Hakemasi lento aseman lentokentän nimi on ja sijainti kunta on:")
            print(*kursori)
            


yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    #en laita salasanaa näkyvillä koska se on public reposity
    password="******",
    autocommit=True
    )



icao = input("Anna hakemasi lentoaseman icao koodi: ")
hakee_lentoaseman_icao(icao)