from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)
app.json.sort_keys = False
@app.route("/kenttä/<icao>")


def hakee_lentoaseman_icao(icao):   
    yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="flight_game",
    user="root",
    #en laita salasanaa näkyvillä koska se on public reposity
    password="123#edcvBnmko=9",
    autocommit=True
    )

    sql = "SELECT name, municipality, ident FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        vastaus = {
            "ICAO": tulos[2],
            "Name": tulos[0],
            "Municipality": tulos[1]
        }
        return vastaus




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
