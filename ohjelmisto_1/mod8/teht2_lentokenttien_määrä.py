import mysql.connector
def Laskee_lentokentät(maakoodi):   
    sql =f"SELECT TYPE,count(*)from airport WHERE iso_country='{maakoodi}' GROUP BY TYPE desc"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print("hakemallassi maalla on näin monta lentokenttää")
        for kursori in tulos:
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



maakoodi = input("Anna hakemasi maasi maakoodi: ")
Laskee_lentokentät(maakoodi)