import _mysql_connector
def hakee_lentoaseman_icao(icao):   
    sql =f"SELECT name, municipality from airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori in tulos:
        print(kursori)
            


yhteys = _mysql_connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="santeri",
    password="Ul485L",
    autocommit=True
    )



icao = input("Anna hakemasi lentoaseman icao koodi: ")
hakee_lentoaseman_icao(icao)