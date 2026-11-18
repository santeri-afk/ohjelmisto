from flask import Flask
import mysql.connector


app = Flask(__name__)
@app.route("/kenttä/<icao>")
yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    #en laita salasanaa näkyvillä koska se on public reposity
    password="******",
    autocommit=True
)

def hakee_lentoaseman_icao(icao):   
    sql =f"SELECT name, municipality from airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for kursori in tulos:
            print(*kursori)


def tulostus(icao):
    koodi = hakee_lentoaseman_icao()
    vastaus = {
        "ICAO": icao,
        "Name": luku1,
        "Municipality": luku2,
        
    }





if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
